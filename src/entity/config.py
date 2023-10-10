import os
import datetime
from src.constant import training_pipeline


class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.datetime.now()):
        timestamp = timestamp.strftime("%m-%d-%Y_%H_%M_%S")
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp 


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
        ##self.data_ingestion_file: str = os.path.join(training_pipeline.PROCESSED_DATA)

        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FEAT_STORE_FILE_NAME)


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_file_path = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.valid_file_name = os.path.join(self.valid_file_path, training_pipeline.DATA_VALIDATION_VALID_FILE_NAME)

      
class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_TRANSFORMATION_DIR)
        self.data_transformation_object = os.path.join(self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR)
        self.data_transformation_file_name = os.path.join(self.data_transformation_object, training_pipeline.DATA_TRANSFORMATION_FILE_NAME)


class ModelTrainerConfig:
    def __init__(self, training_pipleine_config: TrainingPipelineConfig):
        self.data_trainer_dir_name = os.path.join(training_pipleine_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME)
        self.data_trainer_dir = os.path.join(self.data_trainer_dir_name, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR)
        self.data_trainer_file = os.path.join(self.data_trainer_dir, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_NAME)



class ModelPusherConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_pusher_dir_name = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.MODEL_PUSHER_DIR_NAME)
        self.model_pusher_file = os.path.join(self.model_pusher_dir_name, training_pipeline.MODEL_FILE_NAME)
        timestamp = round(datetime.datetime.now().timestamp())
        self.saved_model_path = os.path.join(training_pipeline.SAVED_MODEL_DIR, f"{timestamp}", training_pipeline.MODEL_FILE_NAME)
