from src.datascience.logger import logging
from src.datascience.exception import CustomException
import sys 
from src.datascience.components.data_ingestion import dataingestion
from src.datascience.components.data_ingestion import dataingestionconfig
from src.datascience.components.data_transformation import DataTransformationConfig,DataTransformation
from src.datascience.components.model_trainer import ModelTrainerConfig,ModelTrainer
from src.datascience.utils import evaluate_models

if __name__=="__main__":
     logging.info("the excution is done")

     try:
        # data_ingestion=dataingestionconfig()
         data_ingestion=dataingestion() 
         train_data_path,test_data_path,=data_ingestion.initiate_data_ingestion()
         Data_Transformation_Config=DataTransformationConfig()
         Data_transformation=DataTransformation()
         train_arr,test_arr,_= Data_transformation.initiate_data_transformation(train_data_path,test_data_path)
         model_trainer=ModelTrainer()
         print(model_trainer.initiate_model_trainer(train_arr,test_arr))


     except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)