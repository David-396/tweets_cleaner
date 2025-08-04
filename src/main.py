from src.Manager.manager import Manager

data_file_path = r'..\data\tweets_dataset.csv'
manager = Manager(data_file_path)

manager.run(category_col='Biased',
            text_col='Text',
            remove_punctuation_marks_col='Text',
            col_to_lower='Text',
            save_columns=['Biased','Text'],
            drop_columns=None)