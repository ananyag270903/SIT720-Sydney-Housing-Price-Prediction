# Sydney Housing Price Prediction and Decision Support System

This repository contains the files for the SIT720 Machine Learning
Distinction Task 8.1D.

## Files

- `Task_8.1D.ipynb` - complete data analysis, feature engineering,
  model development, evaluation and comparison.
- `Sydney_Housing_Data_Collection.xlsx` - manually collected dataset
  containing 105 sold properties from Blacktown, Parramatta and Randwick.
- `app.py` - Streamlit housing price prediction application.
- `gradient_boosting_housing_model.pkl` - trained Gradient Boosting
  machine learning pipeline used by the application.
- `requirements.txt` - required Python packages.

## Running the Notebook

Open `Task_8.1D.ipynb` in Jupyter Notebook or JupyterLab and run all cells
from top to bottom. The notebook uses `Sydney_Housing_Data_Collection.xlsx`
as the source dataset.

## Running the Application

Install the required packages:

    pip install -r requirements.txt

Run the Streamlit application:

    streamlit run app.py

The application will open in a web browser. Enter the property
characteristics and select "Predict Sale Price" to generate an estimated
sale price.

## Model

The deployed model is the tuned Gradient Boosting regression model
selected during model evaluation.

## Important Note

The application was developed for an academic machine learning project.
Predictions should be interpreted as estimates and not as professional
property valuations.
