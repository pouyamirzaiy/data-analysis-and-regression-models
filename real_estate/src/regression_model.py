import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import pickle

def train_regression_model(df):
    X = df.drop('house price of unit area', axis=1)
    y = df['house price of unit area']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    model = LinearRegression()
    model.fit(X_train, y_train)
    with open('real_estate_regression_model.pkl', 'wb') as file:
        pickle.dump(model, file)
    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    MAE = metrics.mean_absolute_error(y_test, y_pred)
    MSE = metrics.mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)
    r2 = metrics.r2_score(y_test, y_pred)
    print("Mean Squared Error (MSE): {:.4f}".format(MSE))
    print("R-squared: {:.4f}".format(r2))

if __name__ == "__main__":
    df = pd.read_csv('/content/cleaned_real_estate.csv')
    model, X_test, y_test = train_regression_model(df)
    evaluate_model(model, X_test, y_test)
