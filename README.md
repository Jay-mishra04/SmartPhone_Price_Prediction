# Smartphone Price Prediction (Supervised Machine Learning)

## Introduction
This project aims to predict the price of a smartphone based on various features such as brand, camera quality, battery capacity, and more. The prediction is done using supervised machine learning algorithms.

## Problem Statement
The objective of this project is to develop a machine learning model that can predict the price of any smartphone given inputs like brand, camera, battery, etc. This is a supervised machine learning algorithm, which means it needs a target variable for training the models.

## Dataset
The dataset used in this project was collected through **web scraping** from Flipkart. The dataset contains information about various smartphones with the following columns:

- **Brand**: Names of the brands of the smartphones.
- **Memory**: Information about the ROM and RAM.
- **Camera**: Details about the front and rear cameras, including the number of megapixels.
- **Battery**: Battery size in mAh.
- **Processor**: Processor information categorized into four groups (Mediatek, Snapdragon, Bionic, and others).
- **Ratings**: Ratings given by customers.
- **Reviews**: Number of customers who have rated and reviewed the smartphone.
- **Price**: The price of the smartphone.

### Data Cleaning Steps:
- Removed null values.
- Removed duplicate rows.
- Created separate columns for RAM and ROM.
- Created separate columns for Rear Camera and Front Camera.
- Created separate columns for Reviews and Ratings.
- Converted relevant columns to integer data types.
- Categorized all processors into four groups: Mediatek, Snapdragon, Bionic, and others.
- Summed all the megapixels of the back cameras.
- Removed all non-relevant columns.

### Findings after Data Analysis
- Maximum smartphones have been rated more than 4 out of 5.
- Maximum smartphones have more than 4GB of RAM.
- Maximum smartphones have more than 64GB of ROM.
- Most smartphones have Mediatek processors, followed by Snapdragon.
- Most smartphones have a 5000 mAh battery.
- With increased ratings, the prices of smartphones also increase.
- Apple and Google smartphones are the most expensive.
- Both 4G and 5G smartphones have similar price values.
- The distribution of the price, reviews, and ratings count is highly right-skewed.
- Price has a high positive correlation with ROM.
- Price has a slight positive correlation with back camera, front camera, and RAM.

## Model Implementation and Evaluation
### Machine Learning Models
In this project, I implemented and evaluated three different regression models to predict smartphone prices based on various features. Below is a summary of the models used and their performance metrics:

1. Linear Regression
- Mean Squared Error (MSE): 289,329,933.73
- Root Mean Squared Error (RMSE): 17,009.70
- R² Score: 0.75

2. Random Forest Regressor
- Mean Squared Error (MSE): 31,392,111.47
- Root Mean Squared Error (RMSE): 5,602.87
- R² Score: 0.97

3. XGBoost Regressor
- Mean Squared Error (MSE): 27,825,383.76
- Root Mean Squared Error (RMSE): 5,274.98
- R² Score: 0.98

### Model Pipeline
We created a machine learning pipeline that includes data normalization and the XGBoost Regressor. This pipeline streamlines the process of applying transformations and model fitting.

#### Performance Metrics:
- Mean Squared Error (MSE): 27,825,383.76
- Root Mean Squared Error (RMSE): 5,274.98
- R² Score: 0.98
  
#### Model Saving
The pipeline has been saved for later use. You can load the saved model and use it for making predictions.

## Deployment
The final model is deployed and available for use on Streamlit. You can interact with the deployed model via the following [link](https://smartphonepriceprediction.streamlit.app/)

Feel free to explore the code and documentation provided in this repository to gain a deeper understanding of the project and replicate the results and if you have any questions or suggestions, please don't hesitate to reach out on this [email](jabcd.1997@gmail.com)

Happy forecasting!

