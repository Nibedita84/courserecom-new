from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    data_file_path: str
    ###initial_dump: str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_file_path: str
    valid_file_name: str

@dataclass
class DataTransformationArtifact:
    transformed_data_path: str
    transformed_file: str

@dataclass
class ModelTrainerArtifact:
    trained_model_dir: str


