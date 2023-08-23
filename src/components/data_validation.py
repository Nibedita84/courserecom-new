from src.exception import CourseRecomException
from src.logger import logging
from src.entity.config import DataIngestionConfig
from src.entity.config import DataValidationConfig
from src.entity.artifact import DataIngestionArtifact
from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.entity.artifact import DataValidationArtifact
from src.constant.database import SITE_LINK
from src.data_access.courserecom_data import CourseRecomData
from src.utils import read_yaml_file
import os, sys
import pandas as pd
import requests


class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig, data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CourseRecomException(e, sys)

    ### this checks whether we have all the required columns in the data to ensure we got all the fields while scraping    
    def check_num_of_columns(self, dataframe:pd.DataFrame) -> bool:
        try:
            total_columns = len(self._schema_config["columns"])
            logging.info(f"required number of columns: {total_columns}")
            logging.info(f"columns in the dataframe: {len(dataframe.columns)}")
            if len(dataframe.columns) == total_columns:
                ### create dir and save the file in diractory
                valid_data_file_dir = self.data_validation_config.valid_file_name
                dir_path = os.path.dirname(valid_data_file_dir)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path,exist_ok=True)
                ##fullname = os.path.join(dir_path, self.data_validation_config.valid_file_name)   
                    dataframe.to_csv(self.data_validation_config.valid_file_name, index = False, header = True)

                return True
            return False
        
            
        except Exception as e:
            raise CourseRecomException(e, sys)
        
    ## this method helps read the csv file from the file path
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise CourseRecomException(e,sys)
        

    ### initiating data validation process. this will check for the columns present in the data that we pulled fom the website. 

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            error_message = ""
            data_file = self.data_ingestion_artifact.data_file_path
            data = DataValidation.read_data(data_file)

            logging.info(f'validating number of columns in the dataframe')

            ### validate number of columns
            status = self.check_num_of_columns(dataframe = data)
            if not status:
                error_messsage = f"{error_message} Dataframe doesn't have the required number of columns. \n"

            
            data_validation_artifact = DataValidationArtifact(validation_status = status, valid_file_path = self.data_validation_config.valid_file_path, valid_file_name = self.data_validation_config.valid_file_name)
            

            logging.info(f'Data validation artifact: {data_validation_artifact}')
            return data_validation_artifact

        except Exception as e:
            raise CourseRecomException(e, sys)
                





