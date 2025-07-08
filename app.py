from src.datascience.logger import logging
from src.datascience.exception import CustomException
import sys 
from src.datascience.components.data_ingestion import dataingestion
from src.datascience.components.data_ingestion import dataingestionconfig
if __name__=="__main__":
     logging.info("the excution is done")

     try:
        # data_ingestion=dataingestionconfig()
         data_ingestion=dataingestion() 
         data_ingestion.initiate_data_ingestion()
     except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)