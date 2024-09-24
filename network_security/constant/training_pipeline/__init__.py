import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "NetworkData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"
SAVED_MODEL_DIR =os.path.join("saved_models")

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""



"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""


"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""


"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""



"""
Model Evalaution ralated constant start with MODE TRAINER VAR NAME
"""



