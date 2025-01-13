from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlproject.components.model_tranier import ModelTrainerConfig,MOdelTrainer

import sys



if __name__ == "__main__":
    logging.info("This is a test")

    try:
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        # data_transformation_config=DataTransformationConfig()


        data_transformation=DataTransformation()
        train_array,test_array,_=data_transformation.intiate_data_transformation(train_data_path, test_data_path)

        # model training
        model_trainer=MOdelTrainer()
        print(model_trainer.initiate_model_trainer(train_array, test_array))

    except Exception as e:
        logging.info("This is a custom exception")
        raise CustomException(e,sys)