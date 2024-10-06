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
            self.data_validation_artifact : Data_validation_artifact = data_validation_artifact
            self.data_transformation_config : Data_transformation_config = data_transformation_config
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
            logging.info("Data Transformation started")

            imputer : KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialized KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")

            preprocessor : Pipeline = Pipeline([("imputer", imputer)])

            logging.info("Exited get_data_transformer method")
            return preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def initiate_data_transformation(self) -> Data_transformation_artifact:
        logging.info("Starting data tansformation")
        try:
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            preprocessor = self.get_data_transformer_object()

            logging.info("Preprocessor object obtained")
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis = 1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis = 1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature =preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df) ]
            test_arr = np.c_[ transformed_input_test_feature, np.array(target_feature_test_df) ]

            #save numpy array data
            save_numpy_array_data( self.data_transformation_config.transformed_train_file_path, array=train_arr, )
            save_numpy_array_data( self.data_transformation_config.transformed_test_file_path,array=test_arr,)
            save_object( self.data_transformation_config.transformed_object_file_path, preprocessor_object,)
            
            data_transformation_artifact = Data_transformation_artifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )
            
            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        