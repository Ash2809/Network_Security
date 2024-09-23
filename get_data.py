import json
import pandas as pd
import os
import sys
from dotenv import load_dotenv
import certifi
from network_security.exceptions.exception import NetworkSecurityException
from network_security.logger.logger import logging
import pymongo

ca = certifi.where()
MONGO_URL = os.getenv("MONGO_DB_URL")

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop = True, inplace = True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def push_to_mongo(self, database, records, collection):
        try:
            self.database = database
            self.records = records
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = r"C:\Projects\Network_Security\data\NetworkData.csv"
    network = NetworkDataExtract()
    records = network.csv_to_json(FILE_PATH)

    database = "network_security"
    collection = "net_sec"

    records_ins = network.push_to_mongo(database, records, collection)
