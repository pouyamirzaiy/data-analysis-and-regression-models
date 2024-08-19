import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visualizations(df):
    fig, ax = plt.subplots(2, 3, figsize=(20, 9))
    ax = ax.flatten()

    sns.set()
    sns.lineplot(data=df, x="transaction date", y="house price of unit area", ax=ax[0])
    ax[0].set_title("Price of Unit Area vs. Transaction Date")

    sns.lineplot(data=df, x="house age", y="house price of unit area", ax=ax[1])
    ax[1].set_title("Price of Unit Area vs. House Age")

    sns.lineplot(data=df, x="distance to the nearest MRT station", y="house price of unit area", ax=ax[2])
    ax[2].set_title("Price of Unit Area vs. Distance to the nearest MRT station")

    sns.lineplot(data=df, x="number of convenience stores", y="house price of unit area", ax=ax[3])
    ax[3].set_title("Price of Unit Area vs. no. of Convenience Stores")

    sns.lineplot(data=df, x="latitude", y="house price of unit area", ax=ax[4])
    ax[4].set_title("Price of Unit Area vs. Latitude")

    sns.lineplot(data=df, x="longitude", y="house price of unit area", ax=ax[5])
    ax[5].set_title("Price of Unit Area vs. Longitude")

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('/content/cleaned_real_estate.csv')
    create_visualizations(df)
