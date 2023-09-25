from src.exception import CourseRecomException
from src.logger import logging
from src.entity.config import ModelTrainerConfig 
from src.entity.artifact import ModelTrainerArtifact
from src.entity.config import DataTransformationConfig
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


class ModelTrainer:

    def __init__(self, model_trainer_config = ModelTrainerConfig, data_transformation_artifact = DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact

        except Exception as e:
            raise CourseRecomException(e, sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            return CourseRecomException(e, sys)


    def train_model(self, train_data):
        try:
            cv = CountVectorizer(max_features=5000,stop_words='english')
            vector = cv.fit_transform(train_data['tags1']).toarray()

            similarity = cosine_similarity(vector)
            return similarity
        except Exception as e:
            return CourseRecomException(e, sys) 
        

    def initiate_model_training(self)  -> ModelTrainerArtifact:
        try:
            logging.info("starting model training")
            training_file_path = self.data_transformation_artifact.transformed_file
            model = self.train_model(training_file_path)
            model_dir_path = os.path.dirname(self.model_trainer_config.data_trainer_file)
            os.makedirs(model_dir_path, exist_ok = True)
            pickle.dump(model, open(self.model_trainer_config.data_trainer_file, 'wb'))   ##saving the model
        
            model_trainer_artifact = ModelTrainerArtifact(trained_model_dir = self.model_trainer_config.data_trainer_file)

            logging.info("model training completed")

            return model_trainer_artifact
        except Exception as e:
            raise CourseRecomException(e, sys)

