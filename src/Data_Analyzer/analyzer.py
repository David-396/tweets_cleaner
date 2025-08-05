import numpy as np
import pandas as pd

class Analyzer:
    def __init__(self, dataframe : pd.DataFrame, category_col : str, text_col : str):
        self.dataframe = dataframe.copy()
        self.category_col = category_col
        self.text_col = text_col

        self.category_values = dataframe[self.category_col].unique()
        self.total_df_len = len(self.dataframe)


    ''' analyze 1 - how much tweets each category, uncategorized, sum '''
    def get_tweets_number(self):
        tweets_number_dict = self.dataframe[self.category_col].value_counts().to_dict()

        sum_categorized_tweets = sum(tweets_number_dict.values())
        tweets_number_dict['uncategorized'] = len(self.dataframe[self.category_col]) - sum_categorized_tweets
        tweets_number_dict['total'] = sum(tweets_number_dict.values())

        return tweets_number_dict

    ''' analyze 2 - average tweet length by words '''
    def get_avg_tweet_len(self):
        total_avg = float(self.dataframe[self.text_col].map(lambda text: len(text.split())).sum()) / self.total_df_len
        avg_tweet_len_dict = {'total': total_avg}

        for category in self.category_values:
            category_df = self.dataframe[self.dataframe[self.category_col] == category]
            category_len = len(category_df)

            if category_len:
                category_avg = float(category_df[self.text_col].map(lambda text: len(text.split())).sum()) / category_len
                avg_tweet_len_dict[str(category)] = category_avg

        return avg_tweet_len_dict

    ''' analyze 3 - most 3 longest tweets by letters '''
    def longest_tweets(self, how_much=3):
        categorized_longest_three_tweets = {}

        for category in self.category_values:
            categorized_df = self.dataframe[self.dataframe[self.category_col] == category]

            categorized_df['Len_Text'] = categorized_df[self.text_col].apply(lambda text: len(text))
            longest_tweets = categorized_df.sort_values(by='Len_Text', ascending=False).head(how_much).to_dict()
            categorized_longest_three_tweets[str(category)] = longest_tweets

        return categorized_longest_three_tweets

    ''' analyze 4 - the most 10 common words in tweets '''
    def most_common_words(self, how_much=10):
        all_words = {}

        words_list = " ".join(self.dataframe[self.text_col].values).split()

        for word in words_list:
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

        words_num_series = pd.Series(all_words)
        words_num_series = words_num_series.sort_values(ascending=False).head(how_much).to_dict()

        return words_num_series

    ''' analyze 5 - number of uppercase words each category and total '''
    def uppercase_words_number(self):
        total_uppercase = pd.Series(" ".join(self.dataframe[self.text_col].values).split())
        uppercase_num_dict = {"total_uppercase": int(total_uppercase.str.isupper().sum())}

        for category in self.category_values:
            categorized_df = self.dataframe[self.dataframe[self.category_col] == category][self.text_col]
            words_list = pd.Series(" ".join(categorized_df.values).split())

            uppercase_num_dict[str(category)] = int(words_list.str.isupper().sum())

        return uppercase_num_dict
