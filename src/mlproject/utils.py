import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
# from src.mlproject.utils import read_pgadmin_data

import pandas as pd
from dotenv import load_dotenv
import psycopg2
import pickle
import numpy as np

load_dotenv()

database=os.environ.get("DATABASE")
host = os.environ.get("PGHOST")
user = os.environ.get("PGUSER")
password = os.environ.get("PASSWORD")
port=os.environ.get('PGPORT')


def read_pgadmin_data():
        # Replace these values with your actual database connection details
    logging.info("Reading data from pgadmin4 database")
    try:
        mydb=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            db=database
        )
        logging.info(f"Connection successful: {mydb}")
       
        df=pd.read_sql_query('SELECT * FROM students',mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e, sys)
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)