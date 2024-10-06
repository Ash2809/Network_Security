from datetime import datetime
import os
from network_security.constant import training_pipeline
print(training_pipeline.ARTIFACT_DIR)

class Training_pipeline_config():
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp: str=timestamp

class Data_ingestion_config():
    def __init__(self,training_pipeline_config:Training_pipeline_config):
        self.data_ingestion_dir: str = os.path.join(
                training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
            )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME

class Data_transformation_config():
    def __init__(self,training_pipeline_config:Training_pipeline_config):
        # self.data_transformation_dir: str = os.path.join(Training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        # self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
        #     training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"),)
        # self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
        #     training_pipeline.TEST_FILE_NAME.replace("csv", "npy"), )
        # self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
        #     training_pipeline.PREPROCESSING_OBJECT_FILE_NAME,)
        
        # Access artifact_dir through the instance of training_pipeline_config
        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"))
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, training_pipeline.TEST_FILE_NAME.replace("csv", "npy"))
        self.transformed_object_file_path: str = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, training_pipeline.PREPROCESSING_OBJECT_FILE_NAME)


class Data_validation_config():
    def __init__(self,training_pipeline_config:Training_pipeline_config):
        self.data_validation_dir: str = os.path.join( training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )

class Model_Evaluater_config():
    def __init__(self):
        pass

class Model_trainer_config():
    def __init__(self):
        pass
 
class Model_pusher_config():
    def __init__(self):
        pass