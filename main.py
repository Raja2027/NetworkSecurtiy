from networkSecurity.compenents.data_ingestion import DataIngestion
from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataIngestionConfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataIngestionConfig)
        logging.info("Data ingestion is intitated")
        dataingestionartifact = data_ingestion.initiate_ingestion()
        print(dataingestionartifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)