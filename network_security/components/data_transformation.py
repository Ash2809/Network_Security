import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from network_security.constant.training_pipeline import TARGET_COLUMN
from network_security.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from network_security.entity.artifact_entity import (
    Data_transformation_artifact,
    Data_validation_artifact,
)
from network_security.entity.config_entity import Data_transformation_config
from network_security.exceptions.exception import NetworkSecurityException 
from network_security.logger.logger import logging
#from networksecurity.utils.ml_utils.model.estimator import TargetValueMapping
from network_security.utils.main_utils.utils import save_numpy_array_data, save_object



class DataTransformation():
    def __init__(self, data_validation_artifact : Data_validation_artifact, data_transformation_config : Data_transformation_config):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def get_data_transformer_object(cls) -> Pipeline:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def initiate_data_transformation(self) -> Data_transformation_artifact:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        