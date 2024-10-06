from dataclasses import dataclass

@dataclass
class Data_ingestion_artifact():
    trained_file_path:str
    test_file_path:str

@dataclass
class Data_transformation_artifact():
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class Data_validation_artifact():
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

@dataclass
class Model_Evaluater_artifact():
    pass

@dataclass
class Model_trainer_artifact():
    pass

@dataclass
class Classification_metric_artifact():
    pass

@dataclass 
class Model_pusher_artifact():
    pass