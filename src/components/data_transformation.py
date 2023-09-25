from src.exception import CourseRecomException
from src.logger import logging
from src.entity.config import DataIngestionConfig
from src.entity.config import DataTransformationConfig
from src.entity.config import DataValidationConfig
from src.entity.artifact import DataIngestionArtifact
from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.entity.artifact import DataTransformationArtifact
from src.entity.artifact import DataValidationArtifact
from src.constant.database import SITE_LINK
from src.data_access.courserecom_data import CourseRecomData
from src.utils import read_yaml_file
import os, sys
import pandas as pd
import requests
from ast import literal_eval       ### this is required to be able to avoid any issues while parsing json columns in the dataframe

class DataTransformation:

    def __init__(self, data_transformation_config: DataTransformationConfig, data_validation_artifact: DataValidationArtifact):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            raise CourseRecomException(e, sys)


    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            return CourseRecomException(e, sys)
        
    @staticmethod
    def extract_from_json(text):
        L = []
        for i in text:
            L.append(i['name']) 
        return L
    
    @staticmethod
    def extract_from_json1(text):
        L = []
        for i in text:
            L.append(i['overview']['learn']) 
        return L
    
    @staticmethod
    def remove_extra_characters(text):
        L = []
        for i in text:
            L.append(i.replace(" ",""))
        return L
    
    @staticmethod
    def remove_extra_characters1(text):
        L1 = []
        for i in text:
            for j in i:
                L1.append(j)
        return L1

    

    def transform_data(self) -> DataTransformationArtifact:
        try:
            logging.info("reading the data file")
            df = DataTransformation.read_data(self.data_validation_artifact.valid_file_name)
            df["instructorsDetails1"] = df["instructorsDetails"].apply(literal_eval).apply(DataTransformation.extract_from_json)
            df['learning'] = df['courseMeta'].apply(literal_eval).apply(DataTransformation.extract_from_json1)
            finaldf = df[["index","_id","description","instructorsDetails1", "learning"]]
            finaldf['instructorsDetails1'] = finaldf['instructorsDetails1'].apply(DataTransformation.remove_extra_characters)
            finaldf['description'] = finaldf['learning'].apply(DataTransformation.remove_extra_characters1)
            finaldf['tags'] = finaldf['description'] + finaldf['instructorsDetails1'] +finaldf['learning']
            finaldf['tags1'] = [' '.join(map(str, l)) for l in finaldf['tags']]
            finaldf = finaldf.drop(['instructorsDetails1', 'description','learning'], axis = 1)

            logging.info("file read and transformed. Saving the transformed data file")

            transformed_data_file_dir = self.data_transformation_config.data_transformation_file_name
            dir_path = os.path.dirname(transformed_data_file_dir)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path,exist_ok=True)
                ##fullname = os.path.join(dir_path, self.data_validation_config.valid_file_name)   
                finaldf.to_csv(self.data_transformation_config.data_transformation_file_name, index = False, header = True)

            data_transformation_artifact = DataTransformationArtifact(transformed_data_path = self.data_transformation_config.data_transformation_dir, transformed_file = self.data_transformation_config.data_transformation_file_name)

            logging.info("data transformation complete and file saved")

            return data_transformation_artifact

        except Exception as e:
            raise CourseRecomException(e, sys)
        
    

        
        
         