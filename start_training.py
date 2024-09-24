from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

import os
import sys

from network_security.pipeline.training_pipeline import TrainingPipeline

def start_traninig():
    try:
        logging.info("training has started")

        model_training=TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    start_traninig()
