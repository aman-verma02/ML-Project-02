# Importing required libraries
import os
import sys
from src.exception import CustomException  
from src.logger import logging            
import pandas as pd

from sklearn.model_selection import train_test_split  # To split dataset into train and test sets
from dataclasses import dataclass                     # To create a configuration class with default values


# This class defines configuration paths where the data will be stored
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path to save training dataset
    test_data_path: str = os.path.join('artifacts', 'test.csv')    # Path to save testing dataset
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')      # Path to save raw dataset


# This class handles the whole process of data ingestion
# (reading raw data, saving it, splitting into train/test, and saving them too)
class DataIngestion:
    def __init__(self):
        # Initialize with default config (paths to save data)
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Purpose:
        1. Read raw dataset from a CSV file.
        2. Save raw dataset in 'artifacts/raw.csv'.
        3. Split dataset into training and testing sets.
        4. Save train and test datasets separately.
        """

        logging.info('Data Ingestion method starts')

        try:
            # Step 1: Read dataset
            df = pd.read_csv(r'notebook\data\student.csv')  # Replace with your dataset path
            logging.info('Dataset read as pandas DataFrame')

            # Step 2: Make sure 'artifacts' folder exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Step 3: Save raw dataset to artifacts/raw.csv
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Step 4: Split dataset into train (80%) and test (20%)
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Step 5: Save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            # Return file paths for later use
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Raise custom exception if something goes wrong
            raise CustomException(e, sys)


# This block runs only when this file is executed directly
# (not when imported as a module in another script)
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
