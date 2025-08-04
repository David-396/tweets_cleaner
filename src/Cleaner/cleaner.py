import pandas as pd

class Cleaner:
    def __init__(self, dataframe : pd.DataFrame, category_col):
        self.dataframe = dataframe
        self.category_col = category_col


    ''' save or drop specified columns '''
    def drop_columns(self, save_columns=None|list, drop_columns=None|list):
        if save_columns:
            self.dataframe = self.dataframe[save_columns]

        if drop_columns:
            self.dataframe = self.dataframe.drop(columns=drop_columns)



    ''' drop the uncategorized tweets '''
    def drop_uncategorized_tweets(self):
        self.dataframe.dropna(subset=self.category_col, inplace=True)