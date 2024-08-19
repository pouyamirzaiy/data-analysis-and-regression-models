import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis(df):
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, cmap='YlGnBu', annot=True, linewidths=.5)
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('/content/Real estate.csv')
    df.drop('No', inplace=True, axis=1)
    df.columns = ['transaction date', 'house age', 'distance to the nearest MRT station', 'number of convenience stores', 'latitude', 'longitude', 'house price of unit area']
    correlation_analysis(df)
