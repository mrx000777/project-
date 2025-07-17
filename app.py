from src.datascience.logger import logging
from src.datascience.exception import CustomException
import sys 
from src.datascience.components.data_ingestion import dataingestion
from src.datascience.components.data_ingestion import dataingestionconfig
from src.datascience.components.data_transformation import DataTransformationConfig,DataTransformation
from src.datascience.components.model_trainer import ModelTrainerConfig,ModelTrainer
from src.datascience.utils import evaluate_models
from src.datascience.pipelines.prediction_pipeline import CustomData,PredictPipeline

# if __name__=="__main__":
#      logging.info("the excution is done")

#      try:
#         # data_ingestion=dataingestionconfig()
#          data_ingestion=dataingestion() 
#          train_data_path,test_data_path,=data_ingestion.initiate_data_ingestion()
#          Data_Transformation_Config=DataTransformationConfig()
#          Data_transformation=DataTransformation()
#          train_arr,test_arr,_= Data_transformation.initiate_data_transformation(train_data_path,test_data_path)
#          model_trainer=ModelTrainer()
#          print(model_trainer.initiate_model_trainer(train_arr,test_arr))
#      except Exception as e:
#         logging.info("Custom Exception")
#         raise CustomException(e,sys)
from flask import Flask,request,render_template
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predictdata",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)        
    