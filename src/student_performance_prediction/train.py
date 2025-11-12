# Load required libraries
import pickle

import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def load_data():
    """ 
    Load the dataset
    """
    df = pd.read_csv('src/data/StudentPerformanceFactors.csv')

    # Preprocessing
    df.columns = df.columns.str.lower()

    categorical = df.dtypes[df.dtypes == 'object'].index.to_list()

    for col in categorical:
        df[col] = df[col].str.lower().str.replace(' ', '_').str.strip()
    
    df = df.fillna('Unknown')

    return df


def train_model(df):
    categorical = df.dtypes[df.dtypes == 'object'].index.to_list()
    numerical = [x for x in df.columns if x not in categorical + ['exam_score']]

    pipeline = make_pipeline(
        DictVectorizer(), 
        LinearRegression()
    )

    train_dict = df[categorical + numerical].to_dict(orient='records')
    y_train = df['exam_score']

    pipeline.fit(train_dict, y_train)

    return pipeline


def save_model(filename, model):
    with open(f'src/student_performance_prediction/{filename}', 'wb') as f_out:
        pickle.dump(model, f_out)

    print(f'Save model to {filename}')


if __name__ == '__main__':
    df = load_data()
    pipeline = train_model(df)
    save_model('model.bin', pipeline)
