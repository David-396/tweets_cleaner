import csv
import json
import pandas as pd


class Writer:

    @staticmethod
    def write_to_csv(target_path : str, dataframe : pd.DataFrame):
        dataframe.to_csv(target_path)

    @staticmethod
    def write_to_json(target_path : str, json_data : dict):
        with open(target_path, 'w') as f:
            print(json_data)
            json.dump(json_data, f, indent=4)