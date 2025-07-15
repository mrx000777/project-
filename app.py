from src.datascience.logger import logging
from src.datascience.exception import CustomException
import sys 
from src.datascience.components.data_ingestion import dataingestion
from src.datascience.components.data_ingestion import dataingestionconfig
from src.datascience.components.data_transformation import DataTransformationConfig,DataTransformation
if __name__=="__main__":
     logging.info("the excution is done")

     try:
        # data_ingestion=dataingestionconfig()
         data_ingestion=dataingestion() 
         train_data_path,test_data_path,=data_ingestion.initiate_data_ingestion()
         Data_Transformation_Config=DataTransformationConfig()
         Data_transformation=DataTransformation()
         Data_transformation.initiate_data_transformation(train_data_path,test_data_path)


     except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)