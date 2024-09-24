from dataclasses import dataclass

@dataclass
class Data_ingestion_artifact():
    trained_file_path:str
    test_file_path:str

@dataclass
class Data_transformation_artifact():
    pass

@dataclass
class Data_validation_artifact():
    pass

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