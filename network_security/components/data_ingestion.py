from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split


class DataIngestion():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def data_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def store_data_to_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
