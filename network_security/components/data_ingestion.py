from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.entity.config_entity import Data_ingestion_config
from network_security.entity.artifact_entity import Data_ingestion_artifact

import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

load_dotenv()
MONGO_URL = os.getenv("MONGO_DB_URL")
print(MONGO_URL)

class DataIngestion():
    def __init__(self, data_ingestion_config: Data_ingestion_config):
        try:
            self.data_ingestion_config = data_ingestion_config  
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def data_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name  
            collection_name = self.data_ingestion_config.collection_name  

            self.mongo_client = pymongo.MongoClient(MONGO_URL)
            collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            
            df.replace({"na": np.nan}, inplace=True)
            return df
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def store_data_to_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path  # Fixed incorrect attribute name
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def split_data(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio  # Fixed incorrect attribute name
            )
            logging.info("Performed train test split on the dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)  # Fixed incorrect attribute name
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True  # Fixed incorrect attribute name
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True  # Fixed incorrect attribute name
            )
            logging.info(f"Exported test and train file")
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_ingestion(self):
        try:
            dataframe = self.data_as_dataframe()
            dataframe = self.store_data_to_feature_store(dataframe)  # Pass the dataframe explicitly
            self.split_data(dataframe)

            data_ingestion_artifact = Data_ingestion_artifact(
                trained_file_path=self.data_ingestion_config.training_file_path,  # Fixed incorrect attribute name
                test_file_path=self.data_ingestion_config.testing_file_path  # Fixed incorrect attribute name
            )
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
