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
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

@dataclass
class Model_trainer_artifact():
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact

@dataclass
class Model_evaluation_artifact:
    is_model_accepted: bool
    improved_accuracy: float
    best_model_path: str
    trained_model_path: str
    train_model_metric_artifact: ClassificationMetricArtifact
    best_model_metric_artifact: ClassificationMetricArtifact

@dataclass 
class Model_pusher_artifact():
    pass