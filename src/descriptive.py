import pandas as pd

class DataLoader:
    """Handles loading and saving of data."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None

    def load_csv(self) -> pd.DataFrame:
        """Load Excel file into a DataFrame."""
        try:
            self.data = pd.read_csv(self.filepath)
            print("Data loaded successfully.")

        except Exception as e:
            print(f"Error loading data: {e}")
        return self.data

import os

class Features:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def preprocess(self):
        self.data.fillna(0, inplace=True)
        self.data.drop_duplicates(keep='first')
        columns_to_drop = ['households']  
        self.data.drop(columns=[col for col in columns_to_drop if col in self.data.columns], errors='ignore', inplace=True)
        print(f"removed")
    def save(self, filename: str):
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.data.to_pickle(filename)
        print(f"Data saved as {filename}")

    def generate_summary_statistics(self):
        
        return self.data.describe()

    def check_missing_values(self):

        return self.data.isnull().sum()

    def print_shape(self):
       
        print(f"Data Shape: {self.data.shape}")

    def get_data_types(self):
        
        return self.data.dtypes
    def save(self, filename: str):
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        self.data.to_pickle(filename)
        print(f"Data saved as pickle file: {filename}")
