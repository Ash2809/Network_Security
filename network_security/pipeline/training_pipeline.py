import os
import sys

from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_transformation import DataTransformation
from network_security.components.data_validation import DataValidation
from network_security.components.model_evaluater import ModelEvaluater
from network_security.components.model_pusher import ModelPusher
from network_security.components.model_trainer import ModelTrainer

from network_security.cloud.s3_syncer import S3Sync
from network_security.constant.training_pipeline import TRAINING_BUCKET_NAME
from network_security.constant.training_pipeline import SAVED_MODEL_DIR

from network_security.entity.config_entity import(
    Training_pipeline_config,
    Data_ingestion_config, 
    Data_validation_config, 
    Data_transformation_config, 
    Model_evaluation_config, 
    Model_pusher_config, 
    Model_trainer_config)

from network_security.entity.artifact_entity import(
    Data_ingestion_artifact, 
    Data_transformation_artifact, 
    Data_validation_artifact, 
    Model_evaluation_artifact, 
    Model_pusher_artifact, 
    Model_trainer_artifact, 
    )

class TrainingPipeline():
    def __init__(self):
        self.training_pipepline_config = Training_pipeline_config()  # Correct initialization

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = Data_ingestion_config(training_pipeline_config=self.training_pipepline_config)  # Use correct attribute
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact  
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def start_data_validation(self, data_ingestion_artifact: Data_validation_artifact):
        try:
            data_validation_config = Data_validation_config(training_pipeline_config=self.training_pipepline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=data_validation_config)
            data_ingestion_artifact = data_validation.initiate_data_validation()
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def start_data_transformation(self, data_validation_artifact : Data_validation_artifact):
        try:
            data_transformation_config = Data_transformation_config(training_pipeline_config=self.training_pipepline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=data_transformation_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

        
    def start_model_training(self, data_transformation_artifact: Data_transformation_artifact) -> Model_trainer_artifact:
        try:
            self.model_trainer_config: Model_trainer_config = Model_trainer_config(
                training_pipeline_config=self.training_pipepline_config
            )

            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config,
            )

            model_trainer_artifact = model_trainer.initiate_model_trainer()

            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def start_model_evaluation(self, data_validation_artifact:Data_validation_artifact, model_trainer_artifact:Model_trainer_artifact,):
        try:
            model_evaluation_config:Model_evaluation_config=Model_evaluation_config(training_pipeline_config=self.training_pipepline_config)
            model_eval=ModelEvaluater(model_evaluation_config,Data_validation_artifact,model_trainer_artifact)
            model_eval_artifact=model_eval.initiate_model_evaluation()
            return  model_eval_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_model_pusher(self, model_eval_artifact:Model_evaluation_artifact):
        try:
            model_pusher_config = Model_pusher_config(training_pipeline_config=self.training_pipepline_config)
            model_pusher = ModelPusher(model_pusher_config, model_eval_artifact)
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def sync_artifact_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipepline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(folder = self.training_pipepline_config.artifact_dir,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    def sync_saved_model_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/{SAVED_MODEL_DIR}"
            self.s3_sync.sync_folder_to_s3(folder = SAVED_MODEL_DIR,aws_bucket_url=aws_bucket_url)
        except Exception as e:
            raise NetworkSecurityException(e,sys)  
        
    def run_pipeline(self):
        try:
            ingestion_artifact = self.start_data_ingestion()
            print("ingestion artifact:")
            print("Starting validation")
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=ingestion_artifact)
            print("Data Validation Artifact is: ")
            print("Starting Data Transformation")
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            print("Artifact of transformation: ")
            model_trainer_artifact=self.start_model_training(data_transformation_artifact=data_transformation_artifact)
            print("Artifact of training")
            model_eval_artifact=self.start_model_evaluation(data_validation_artifact=data_validation_artifact,model_trainer_artifact=model_trainer_artifact)
            if not model_eval_artifact.is_model_accepted:
                #raise Exception("Trained model is not better than the best model")
                print("Trained model is not better than the best model")
            print("model evalaution artifact.")

            model_pusher_artifact = self.start_model_pusher(model_eval_artifact)
            print("Model pushing complete")

            TrainingPipeline.is_pipeline_running=False
            self.sync_artifact_dir_to_s3()
            self.sync_saved_model_dir_to_s3()
        except Exception as e:
            self.sync_artifact_dir_to_s3()
            TrainingPipeline.is_pipeline_running=False
            raise NetworkSecurityException(e,sys)
       
