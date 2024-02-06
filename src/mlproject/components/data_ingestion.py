import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split


@dataclass
class DataingestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    rav_data_path:str=os.path.join('artifacts','rav.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(os.path.join('notebook/data','rav.csv'))
            logging.info("reading complated mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.rav_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=1)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("data ingestion complited")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                    )

            
        except Exception as e:
            raise CustomException(e,sys)