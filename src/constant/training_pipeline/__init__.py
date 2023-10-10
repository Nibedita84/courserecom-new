import os

SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME: str = "model.pkl"
##PROCESSED_DATA: str = "extracted_data.csv"
##FETCHED_DATA: str = "fetched_data"

### Defining common constant variables for training Pipeline
DATA_LINK = 'https://ineuron.ai/courses'
PIPELINE_NAME: str = "courserecom"
ARTIFACT_DIR: str = "artifact"
FEAT_STORE_FILE_NAME: str = "courserecom.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")



### Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME: str = "courserecom"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"



### Data Validation Constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_VALID_FILE_NAME : str = "valid_data.csv"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


### Data Transformation Constants

DATA_TRANSFORMATION_DIR: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
DATA_TRANSFORMATION_FILE_NAME: str = "transformed_data.csv"

### Model Trainer Constants

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"




### Model Pusher Constants

MODEL_PUSHER_DIR_NAME: str = "model_pusher"
MODEL_PUSHER_SAVED_MODEL_DIR: str = SAVED_MODEL_DIR


