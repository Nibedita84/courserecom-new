import os

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





### Model Evaluation Constants



