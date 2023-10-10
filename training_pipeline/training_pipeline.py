from src.logger import logging
from src.exception import CourseRecomException
from src.data_access.courserecom_data import CourseRecomData
from src.components.data_ingestion import DataIngestion
from src.entity.config import DataIngestionConfig
from src.entity.artifact import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact, ModelTrainerArtifact, ModelPusherArtifact
from src.entity.config import DataValidationConfig, DataTransformationConfig
from src.components.data_validation  import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.entity.config import ModelTrainerConfig
from src.entity.config import TrainingPipelineConfig
from src.entity.config import ModelPusherConfig
from src.components.model_pusher import ModelPusher
from src.entity.artifact import ModelPusherArtifact
from src.constant import training_pipeline
from src.constant.database import SITE_LINK
from src.constant.training_pipeline import SCHEMA_FILE_PATH, SAVED_MODEL_DIR
from src.cloud_storage.s3_syncer import S3sync
from src.constant.s3_bucket import TRAINING_BUCKET_NAME
import pandas as pd
import pickle

import sys


class TrainingPipeline:
    is_pipeline_running = False
    
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        self.s3_sync = S3sync()



    def start_data_ingestion(self) -> DataIngestionArtifact:
        try: 
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config = self.training_pipeline_config)
            logging.info('Starting Data Ingestion')
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise CourseRecomException(e,sys)
        
    
    def start_data_validation(self, data_ingestion_artifact = DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact = data_ingestion_artifact, data_validation_config = data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise CourseRecomException(e, sys)
        
    def start_data_transformation(self, data_validation_artifact = DataValidationArtifact) -> DataTransformationArtifact:
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config = self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact = data_validation_artifact, data_transformation_config = data_transformation_config)
            data_transformation_artifact = data_transformation.transform_data()
            return data_transformation_artifact
    
        except Exception as e:
            raise CourseRecomException(e, sys)
        

    def start_model_trainer(self, data_transformation_artifact = DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            model_trainer_config = ModelTrainerConfig(training_pipleine_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(data_transformation_artifact = data_transformation_artifact, model_trainer_config = model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_training()
            return model_trainer_artifact

        except Exception as e:
            raise CourseRecomException(e, sys)
        
    def start_model_pusher(self, model_trainer_artifact = ModelPusherArtifact) -> ModelPusherArtifact:
        try:
            model_pusher_config = ModelPusherConfig(training_pipeline_config = self.training_pipeline_config)
            model_pusher = ModelPusher(model_trainer_artifact = model_trainer_artifact, model_pusher_config = model_pusher_config)
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            return model_pusher_artifact
        except Exception as e:
            raise CourseRecomException(e, sys)
        

    """def sync_artifact_dir_to_s3(self):
        try:
            aws_buket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(folder = self.training_pipeline_config.artifact_dir,aws_buket_url=aws_buket_url)
        except Exception as e:
            raise CourseRecomException(e,sys)
            
    def sync_saved_model_dir_to_s3(self):
        try:
            aws_buket_url = f"s3://{TRAINING_BUCKET_NAME}/{SAVED_MODEL_DIR}"
            self.s3_sync.sync_folder_to_s3(folder = SAVED_MODEL_DIR,aws_buket_url=aws_buket_url)
        except Exception as e:
            raise CourseRecomException(e,sys)
      """  

    def run_pipeline(self):
        try:
            logging.info("starting the pipeline")
            TrainingPipeline.is_pipeline_running = True

            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            logging.info("data ingestion completed")
            data_validation_artifact:DataValidationArtifact = self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)
            logging.info("data validation completed")
            data_transformation_artifact: DataTransformationArtifact = self.start_data_transformation(data_validation_artifact = data_validation_artifact)
            logging.info("data transformation completed")
            model_trainer_artifact: ModelTrainerArtifact = self.start_model_trainer(data_transformation_artifact = data_transformation_artifact)
            model_pusher_artifact: ModelPusherArtifact = self.start_model_pusher(model_trainer_artifact = model_trainer_artifact)

            logging.info("model saved")
            

            TrainingPipeline.is_pipeline_running = False
            ##self.sync_artifact_dir_to_s3()
            ##self.sync_saved_model_to_s3()

        except Exception as e:
            ###self.sync_artifact_dir_to_s3()
            TrainingPipeline.is_pipeline_running = False
            raise CourseRecomException(e, sys)
 


        
     
        


