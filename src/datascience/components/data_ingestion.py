import os
import sys
from src.datascience.exception import CustomException
from src.datascience.logger import logging
import pandas as pd 
from src.datascience.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
@dataclass
class dataingestionconfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")
class dataingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()
    def initiate_data_ingestion(self):
        try:
           df=pd.read_csv(os.path.join("notebook/data","raw.csv"))
           logging.info("reading completed my sql database ")
           os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
           df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
           train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
           train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
           test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
           logging.info("data ingestion is completed ")
           return(
               self.ingestion_config.train_data_path,
               self.ingestion_config.test_data_path
           )


        except Exception as  e:
            raise CustomException(e,sys)
