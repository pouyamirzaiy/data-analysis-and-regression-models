import pandas as pd

def clean_data(df):
    df.drop('No', inplace=True, axis=1)
    df.columns = ['transaction date', 'house age', 'distance to the nearest MRT station', 'number of convenience stores', 'latitude', 'longitude', 'house price of unit area']
    df = df[df['house price of unit area'] < 80]
    df = df[df['distance to the nearest MRT station'] < 3000]
    df = df[df['longitude'] > 121.50]
    return df

if __name__ == "__main__":
    df = pd.read_csv('/content/Real estate.csv')
    df = clean_data(df)
    df.to_csv('/content/cleaned_real_estate.csv', index=False)
