# CONTENT-MONETIZATION-MODELER_project
Machine learning project for YouTube ad revenue prediction using regression models and Streamlit.

# Content Monetization Modeler

## YouTube Ad Revenue Prediction

### Project Overview

Content Monetization Modeler is a machine learning project that predicts estimated YouTube advertising revenue based on video performance and contextual information.

### Objective

The objective of this project is to build regression models that predict the target variable `ad_revenue_usd`.

### Dataset

The dataset contains YouTube video-related information such as:

- Views
- Likes
- Comments
- Watch time
- Video length
- Subscribers
- Category
- Device
- Country
- Ad revenue

The dataset contains approximately 122,400 records and 12 original columns.

### Data Preprocessing

The following preprocessing steps were performed:

- Missing value analysis
- Duplicate detection and removal
- Numerical missing-value imputation using median values
- Categorical missing-value handling
- One-Hot Encoding
- Feature scaling

### Feature Engineering

The following features were created:

- `engagement_rate` = (likes + comments) / views
- `watch_time_per_minute` = watch_time_minutes / video_length_minutes
- `views_per_subscriber` = views / subscribers

The `video_id` column was excluded because it is an identifier.

The supplied `date` field was excluded from predictive modeling because its values were not in a usable calendar-date format.

### Machine Learning Models

Five regression models were evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regression
5. Random Forest Regression

### Evaluation Metrics

The models were evaluated using:

- R² Score
- RMSE
- MAE

The best-performing model was selected based on the highest R² Score and saved as `model.pkl`.

### Streamlit Application

A Streamlit application was developed to allow users to enter video information and receive an estimated YouTube advertising revenue prediction.

The application automatically calculates the engineered features and uses the trained model to generate the prediction.

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

### Project Structure

```text
Content_Monetization_Modeler/
│
├── app.py
├── model.pkl
├── content_monetization_modeler.ipynb
├── youtube_ad_revenue_dataset.csv
├── model_comparison.csv
├── cleaned_youtube_revenue_data.csv
├── requirements.txt
└── README.md
