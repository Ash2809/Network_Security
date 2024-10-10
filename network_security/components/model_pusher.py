from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging

from network_security.entity.artifact_entity import Model_pusher_artifact, Model_trainer_artifact, Model_evaluation_artifact
from network_security.entity.config_entity import Model_evaluation_config, Model_pusher_config

from network_security.utils.ml_utils.metric.classification_metric import get_classification_score
from network_security.utils.main_utils.utils import save_object,load_object,write_yaml_file

import shutil
import os,sys

class ModelPusher():
    def __init__(self,model_pusher_config:Model_pusher_config, model_eval_artifact:Model_evaluation_artifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_model_pusher(self,)->Model_pusher_artifact:
        try:
            trained_model_path = self.model_eval_artifact.trained_model_path
            
            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path),exist_ok=True)
            shutil.copy(src=trained_model_path, dst=model_file_path)

            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path),exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            model_pusher_artifact = Model_pusher_artifact(saved_model_path=saved_model_path, model_file_path=model_file_path)
            return model_pusher_artifact
        except  Exception as e:
            raise NetworkSecurityException(e, sys)