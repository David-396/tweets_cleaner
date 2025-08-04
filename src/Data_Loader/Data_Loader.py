import pandas as pd


class Loader:
    def __init__(self, file_path):
        self.path = file_path
        self.data_frame = self.load_data()

    def load_data(self):
        dataframe = pd.read_csv(self.path)
        return dataframe