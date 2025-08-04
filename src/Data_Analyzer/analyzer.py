import pandas as pd

class Analyzer:
    def __init__(self, dataframe : pd.DataFrame, category_col : str, text_col : str):
        self.dataframe = dataframe
        self.category_col = category_col
        self.text_col = text_col
        self.category_values = dataframe[self.category_col].unique()
        self.total_df_len = len(self.dataframe)


    ''' analyze 1 - how much tweets each category, uncategorized, sum '''
    def get_tweets_number(self):
        tweets_number_dict = self.dataframe[self.category_col].value_counts().to_dict()

        sum_categorized_tweets = sum(tweets_number_dict.values())
        tweets_number_dict['uncategorized'] = len(self.dataframe[self.category_col]) - sum_categorized_tweets
        tweets_number_dict['sum_tweets'] = sum(tweets_number_dict.values())

        return tweets_number_dict


    ''' analyze 2 - average tweet length each tweet '''
    def get_avg_tweet_len(self):
        avg_tweet_len_dict = {}

        for category in self.category_values:

            category_df = self.dataframe[self.dataframe[self.category_col] == category]

            category_len = len(category_df)

            category_avg = sum(category_df[self.text_col].map(lambda text: len(text.split()))) / category_len

            avg_tweet_len_dict[category] = category_avg


        avg_tweet_len_dict['total_avg'] = sum(self.dataframe[self.text_col].map(lambda text: len(text.split()))) / self.total_df_len
        return avg_tweet_len_dict


