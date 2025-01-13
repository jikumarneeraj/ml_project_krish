from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation

import sys



if __name__ == "__main__":
    logging.info("This is a test")

    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        # data_transformation_config=DataTransformationConfig()


        data_transformation=DataTransformation()
        data_transformation.intiate_data_transformation(train_data_path, test_data_path)
        
    except Exception as e:
        logging.info("This is a custom exception")
        raise CustomException(e,sys)