from src.logger import logging
from src.exception import CourseRecomException
from src.data_access.courserecom_data import CourseRecomData
from src.components.data_ingestion import DataIngestion
from src.entity.config import DataIngestionConfig
from src.entity.artifact import DataIngestionArtifact, DataTransformationArtifact
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
from src.constant.training_pipeline import SCHEMA_FILE_PATH
import sys


"""if __name__ == "__main__":
    logging.info("starting data ingestion")
    try:
        x = DataIngestion(data_ingestion_config=DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig()))
        data = x.initiate_data_ingestion()
        print(data)
    except Exception as e:
        raise CourseRecomException(e, sys)
   """ 
   
if __name__ == "__main__":
    try:
        data_ingest = DataIngestion(data_ingestion_config=DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig()))
        x = DataValidation(DataValidationConfig(TrainingPipelineConfig()), data_ingest.initiate_data_ingestion())
        y = DataTransformation(DataTransformationConfig(TrainingPipelineConfig()), x.initiate_data_validation())
        z = ModelTrainer(ModelTrainerConfig(TrainingPipelineConfig()),y.transform_data())
        a = ModelPusher(ModelPusherConfig(TrainingPipelineConfig()), z.initiate_model_training())
        a.initiate_model_pusher()
        ###x.initiate_data_validation()

    except Exception as e:
        raise CourseRecomException(e, sys)
    
