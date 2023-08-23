from src.exception import CourseRecomException
from src.logger import logging
from src.entity.config import DataIngestionConfig
from src.entity.artifact import DataIngestionArtifact
from src.constant.database import SITE_LINK
from src.data_access.courserecom_data import CourseRecomData
import os, sys
import pandas as pd
import requests


class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CourseRecomException(e, sys)
        

    def export_data_into_feature_store(self, link)  -> pd.DataFrame:
        try:
            logging.info("saving data into the feature store")
            scrape = CourseRecomData()
            data = scrape.scrape_and_save_to_dataframe(link)
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            ## create the folder to store feature store
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path)
            data.to_csv(feature_store_file_path, index = False, header = True)
            logging.info("saved the data to the feature store file")
            return data
        
        except Exception as e:
            raise CourseRecomException(e, sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store(SITE_LINK)
            data_ingestion_artifact = DataIngestionArtifact(data_file_path= self.data_ingestion_config.feature_store_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise CourseRecomException(e, sys) 
               
            
        








