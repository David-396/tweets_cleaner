from src.Cleaner.cleaner import Cleaner
from src.Data_Analyzer.analyzer import Analyzer
from src.Data_Loader.Data_Loader import Loader
from src.Writer.writer import Writer


class Manager:
    def __init__(self, file_data_path):
        self.file_data_path = file_data_path
        self.dataframe = None
        self.analyzed_data = {}
        self.clean_dataframe = None

    ''' load to dataframe '''
    def load_to_df(self):
        loader = Loader(self.file_data_path)
        self.dataframe = loader.dataframe

    ''' analyze the data '''
    def data_analyze(self, category_col : str,
                     text_col : str):

        analyzer = Analyzer(self.dataframe, category_col, text_col)
        # 1
        self.analyzed_data['tweets_number'] = analyzer.get_tweets_number()
        # 2
        self.analyzed_data['average_tweet_len'] = analyzer.get_avg_tweet_len()
        # 3
        self.analyzed_data['longest_3_tweets'] = analyzer.longest_tweets(3)
        # 4
        self.analyzed_data['most_common_words'] = analyzer.most_common_words(10)
        # 5
        self.analyzed_data['uppercase_words_number'] = analyzer.uppercase_words_number()

    ''' write to json '''
    def analyzed_data_writer(self):
        target_path = r'C:\Users\User\OneDrive\Desktop\tweets_cleaner\results\results.json'
        Writer.write_to_json(target_path, self.analyzed_data)

    ''' clean the df '''
    def df_cleaner(self, category_col : str,
                   remove_punctuation_marks_col : str,
                   col_to_lower : str,
                   save_columns=None|list,
                   drop_columns=None|list):

        cleaner = Cleaner(self.dataframe, category_col)

        # 1
        cleaner.drop_columns(save_columns=save_columns, drop_columns=drop_columns)
        # 2
        cleaner.remove_punctuation_marks(remove_punctuation_marks_col)
        # 3
        cleaner.col_to_lower(col_to_lower)
        # 4
        cleaner.drop_uncategorized_tweets()

        self.clean_dataframe = cleaner.dataframe

    ''' write to csv '''
    def cleaned_df_writer(self):
        target_path = r'C:\Users\User\OneDrive\Desktop\tweets_cleaner\results\cleaned_dataset_tweets.csv'
        Writer.write_to_csv(target_path, self.clean_dataframe)


    ''' main func '''
    def run(self, category_col : str,
            text_col : str,
            remove_punctuation_marks_col : str,
            col_to_lower : str,
            save_columns=None|list,
            drop_columns=None|list):

        # loader
        self.load_to_df()
        # analyzer
        self.data_analyze(category_col, text_col)
        # analyze data writer
        self.analyzed_data_writer()
        # cleaner
        self.df_cleaner(category_col=category_col,
                        remove_punctuation_marks_col=remove_punctuation_marks_col,
                        col_to_lower=col_to_lower,
                        save_columns=save_columns,
                        drop_columns=drop_columns)
        # clean df writer
        self.cleaned_df_writer()







