import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
import sys, os
from src.logger import logging

import requests
from src.exception import CourseRecomException

class CourseRecomData:

    def __init__(self):
        try:
            logging.info(f'create class object')
        except Exception as e:
            raise CourseRecomException(e, sys)
    

    def scrape_and_save_to_dataframe(self, link): 
        try:
            res = requests.get(link) 
            ###txt = res.text
            ###status = res.status_code
            soup = BeautifulSoup(res.content, 'html.parser')   #### extracting the website content
            div = soup.find_all('script', {"type": "application/json"})   ###finding and extracting the data/type we are intereseted in 

            for data in div:
                jsn = json.loads(data.string)   ## parsing the json content of the website

            final_data = jsn['props']['pageProps']['initialState']['init']    ### extracting and saving the details we want for our model
            
            modified_data = pd.DataFrame(final_data['courses']).transpose().reset_index()

            return modified_data
        except Exception as e:
            raise CourseRecomException(e, sys)
        


        



        