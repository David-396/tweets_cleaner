import pandas as pd

class Cleaner:
    def __init__(self, dataframe : pd.DataFrame, category_col):
        self.dataframe = dataframe
        self.category_col = category_col
        self.punctuation_marks = ['.', ',']


    ''' save or drop specified columns '''
    def drop_columns(self, save_columns=None|list, drop_columns=None|list):
        if save_columns:
            self.dataframe = self.dataframe[save_columns]

        if drop_columns:
            self.dataframe = self.dataframe.drop(columns=drop_columns)

    ''' converting column to lowercase '''
    def col_to_lower(self, column):
        self.dataframe[column] = self.dataframe[column].apply(lambda text: text.lower())

    ''' drop the uncategorized tweets '''
    def drop_uncategorized_tweets(self):
        self.dataframe.dropna(subset=self.category_col, inplace=True)