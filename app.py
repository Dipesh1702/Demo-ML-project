from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataingestionConfig
from src.mlproject.components.data_transformation import DatatransformationConfig,Datatranformation
from src.mlproject.components.model_trainer import ModelTrainerConfig,ModelTrainer
import sys


if __name__=="__main__":
    logging.info("The exicution has started")

    try:
        # data_ingestion_config=DataingestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_tranformation_config=DatatransformationConfig()
        data_transformation=Datatranformation()
        train_arr,test_arr,_=data_transformation.initiate_data_tranformation(train_data_path,test_data_path)
        
        #model trainer
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
    except Exception as e:
        raise CustomException(e, sys)

