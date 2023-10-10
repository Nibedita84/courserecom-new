from src.exception import CourseRecomException
from src.logger import logging
from src.entity.config import ModelTrainerConfig 
from src.entity.artifact import ModelTrainerArtifact
from src.entity.config import DataTransformationConfig
from src.entity.config import ModelPusherConfig
from src.entity.artifact import ModelPusherArtifact
from src.entity.config import DataValidationConfig
from src.entity.artifact import DataIngestionArtifact
from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.entity.artifact import DataTransformationArtifact
from src.entity.artifact import DataValidationArtifact
from src.constant.database import SITE_LINK
from src.data_access.courserecom_data import CourseRecomData
from src.utils import read_yaml_file
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os, sys
import pandas as pd
import pickle
import shutil



class ModelPusher:

    def __init__(self, model_pusher_config = ModelPusherConfig, model_trainer_artifact = ModelTrainerArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise CourseRecomException(e, sys)
        

    def initiate_model_pusher(self,) -> ModelPusherArtifact:
        try:
            logging.info("initiating model pushing to save the model")
            trained_model_path = self.model_trainer_artifact.trained_model_dir
            
            model_file_path = self.model_pusher_config.model_pusher_file
            os.makedirs(os.path.dirname(model_file_path), exist_ok= True)
            shutil.copy(src = trained_model_path, dst = model_file_path)

            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok = True)
            shutil.copy(src = trained_model_path, dst = saved_model_path)

            model_pusher_artifact = ModelPusherArtifact(saved_model_path = saved_model_path, model_file_path = model_file_path)

            logging.info("successfully saved the model in the location")

            return model_pusher_artifact
        except Exception as e:
            raise CourseRecomException(e, sys) 
        
        
        