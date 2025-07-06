from src.datascience .logger import logging
from src.datascience .exception import CustomException
import sys 
if __name__=="__main__":
     logging.info("the excution is done")

     try:
          a=1/0
         
     except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)