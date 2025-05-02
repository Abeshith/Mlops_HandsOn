import os, sys, json
from dotenv import load_dotenv
from network_security.logging.logger import logging
from network_security.exceptions.exception import NetworkSecurityException
import pymongo


load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

### MongoDB Connection - for making the secure http using certifi to ensure only to trust only valid cetificates ###
import certifi
ca = certifi.where()

import pandas as pd 
import numpy as np

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)

            data.reset_index(drop=True, inplace=True)

            records = json.loads(data.to_json(orient='records'))

            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongo(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)

            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            
            logging.info("Data inserted successfully into MongoDB")
            return len(self.records)
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
        FILE_PATH = "network_data\phisingData.csv"
        DATABASE = "network_security"
        Collection = "phishing_data"

        network_data = NetworkDataExtract()
        records = network_data.csv_to_json(FILE_PATH)
        print(f"Number of records in the CSV file: {records}")
        number_of_records = network_data.insert_data_to_mongo(records, DATABASE, Collection)
        print(f"Number of records inserted: {number_of_records}")



           

