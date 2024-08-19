# **Real Estate Price Prediction and Life Expectancy Analysis**

## **Project Overview**

This project consists of two main parts:

1. **Real Estate Price Prediction**: Analyzing and predicting real estate prices based on various features such as transaction date, house age, distance to the nearest MRT station, number of convenience stores, latitude, and longitude.
2. **Life Expectancy Analysis**: Analyzing life expectancy data from the World Health Organization (WHO) to identify patterns and correlations with various factors such as GDP, population, and health indicators.

## **Installation Instructions**

To run this project, you'll need to have Python installed along with the following libraries:

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- scipy

You can install these libraries using pip:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn scipy
```

## **Usage**

### **Real Estate Price Prediction**

1. Load the dataset:

   ```python
   df = pd.read_csv('/content/Real estate.csv')
   ```

2. Clean and preprocess the data:

   ```python
   df.drop('No', inplace=True, axis=1)
   df.columns = ['transaction date', 'house age', 'distance to the nearest MRT station', 'number of convenience stores', 'latitude', 'longitude', 'house price of unit area']
   ```

3. Perform exploratory data analysis (EDA) and visualize the data:

   ```python
   sns.lineplot(data=df, x="transaction date", y="house price of unit area")
   ```

4. Train a linear regression model:

   ```python
   from sklearn.linear_model import LinearRegression
   model = LinearRegression()
   model.fit(X_train, y_train)
   ```

5. Evaluate the model:
   ```python
   y_pred = model.predict(X_test)
   ```

### **Life Expectancy Analysis**

1. Load the dataset:

   ```python
   data = pd.read_csv("/content/Life Expectancy Data.csv")
   ```

2. Clean and preprocess the data:

   ```python
   data.drop("under-five deaths ", axis=1, inplace=True)
   ```

3. Perform exploratory data analysis (EDA) and visualize the data:

   ```python
   sns.heatmap(data[num_columns].corr(), cmap='Blues', linewidths=3, annot=True)
   ```

4. Conduct statistical tests:
   ```python
   from scipy.stats import ttest_ind
   t_statistic, p_value = ttest_ind(developed['Hepatitis B'].dropna(), developing['Hepatitis B'].dropna(), equal_var=False)
   ```

## **Features**

- **Real Estate Price Prediction**:

  - Data cleaning and preprocessing
  - Exploratory data analysis (EDA)
  - Outlier detection and removal
  - Correlation analysis
  - Linear regression model training and evaluation

- **Life Expectancy Analysis**:
  - Data cleaning and preprocessing
  - Exploratory data analysis (EDA)
  - Outlier detection and removal
  - Correlation analysis
  - Statistical tests (t-tests)

## **Contributing**

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## **License**

This project is licensed under the MIT License.

## **Contact Information**

If you have any questions or feedback, feel free to reach out to me at pouya.8226@gmail.come
