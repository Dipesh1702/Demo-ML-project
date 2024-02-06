from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataingestionConfig
from src.mlproject.components.data_transformation import DatatransformationConfig,Datatranformation
import sys


if __name__=="__main__":
    logging.info("The exicution has started")

    try:
        # data_ingestion_config=DataingestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_tranformation_config=DatatransformationConfig()
        data_transformation=Datatranformation()
        data_transformation.initiate_data_tranformation(train_data_path,test_data_path)
    except Exception as e:
        raise CustomException(e, sys)

