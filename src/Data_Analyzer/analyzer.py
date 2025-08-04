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


    ''' analyze 3 - most 3 biggest tweets in chars '''
    def longest_three_tweets(self):
        categorized_longest_three_tweets = {}

        for category in self.category_values:
            categorized_df = self.dataframe[self.dataframe == category]

            categorized_df['Len_Text'] = categorized_df[self.text_col].apply(lambda text: len(text))
            longest_tweets = categorized_df.sort_values(by='Len_Text', ascending=False).head(3).to_dict()
            categorized_longest_three_tweets[category] = longest_tweets

        return categorized_longest_three_tweets


    ''' analyze 4 - the most 10 common words in the text '''
    def most_common_words(self):
        all_words = {}

        words_list = " ".join(self.dataframe[self.text_col].values).split()

        for word in words_list:

            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1


        words_num_series = pd.Series(all_words)
        words_num_series = words_num_series.sort_values(ascending=False).head(10).to_dict()

        return words_num_series


    ''' analyze 5 - number of uppercase words each category and total '''
    def uppercase_words_number(self):
        total_uppercase = pd.Series(" ".join(self.dataframe[self.text_col].values).split())
        uppercase_num_dict = {"total_uppercase": sum(total_uppercase.str.isupper())}

        for category in self.category_values:
            categorized_df = self.dataframe[self.dataframe[self.category_col] == category]
            words_list = pd.Series(" ".join(categorized_df[self.text_col].values).split())

            uppercase_num_dict[category] = sum(words_list.str.isupper())

        return uppercase_num_dict
