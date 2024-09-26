from network_security.entity.artifact_entity import Data_validation_artifact, Data_ingestion_artifact
from network_security.entity.config_entity import Data_validation_config

from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

import pandas as pd
import os
import sys

class DataValidation():
    def __init__(self, data_ingestion_artifact : Data_ingestion_artifact, data_validation_config : Data_validation_config):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def detect_numerical_columns(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    

    def is_numerical_column_exist(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    @staticmethod
    def read_data(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def detect_dataset_drift(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def initiate_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)