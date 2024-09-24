import os
import sys

from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_transformation import DataTransformation
from network_security.components.data_validation import DataValidation
from network_security.components.model_evaluater import ModelEvaluater
from network_security.components.model_pusher import ModelPusher
from network_security.components.model_training import ModelTrainer

from network_security.entity.config_entity import(
    Training_pipeline_config,
    Data_ingestion_config, 
    Data_validation_config, 
    Data_transformation_config, 
    Model_Evaluater_config, 
    Model_pusher_config, 
    Model_trainer_config)

from network_security.entity.artifact_entity import(
    Data_ingestion_artifact, 
    Data_transformation_artifact, 
    Data_validation_artifact, 
    Model_Evaluater_artifact, 
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
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_training(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def run_pipeline(self):
        try:
            ingestion_artifact = self.start_data_ingestion()
            print(ingestion_artifact)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
