import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Content Monetization Modeler",
    page_icon="📺",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("📺 Content Monetization Modeler")

st.markdown(
    """
    ### YouTube Ad Revenue Prediction

    This application predicts the estimated advertising
    revenue of a YouTube video using video performance
    and contextual information.
    """
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load("C:\\Users\\ABHISHEK\Documents\\Data Science\\CONTENT MONETIZATION MODELER_project\\model.pkl")


try:

    model = load_model()

except Exception as e:

    st.error(
        "Unable to load model.pkl. "
        "Please run the Jupyter Notebook first "
        "and make sure model.pkl is present."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("🎥 Enter Video Details")


views = st.sidebar.number_input(
    "Views",
    min_value=0,
    value=10000,
    step=100
)


likes = st.sidebar.number_input(
    "Likes",
    min_value=0,
    value=500,
    step=10
)


comments = st.sidebar.number_input(
    "Comments",
    min_value=0,
    value=50,
    step=10
)


watch_time_minutes = st.sidebar.number_input(
    "Watch Time (Minutes)",
    min_value=0.0,
    value=1000.0
)


video_length_minutes = st.sidebar.number_input(
    "Video Length (Minutes)",
    min_value=0.1,
    value=10.0
)


subscribers = st.sidebar.number_input(
    "Subscribers",
    min_value=0,
    value=10000,
    step=100
)


category = st.sidebar.selectbox(
    "Category",
    [
        "Entertainment",
        "Gaming",
        "Education",
        "Music",
        "Tech",
        "Lifestyle"
    ]
)


device = st.sidebar.selectbox(
    "Device",
    [
        "TV",
        "Tablet",
        "Mobile",
        "Desktop"
    ]
)


country = st.sidebar.selectbox(
    "Country",
    [
        "IN",
        "CA",
        "UK",
        "US",
        "DE",
        "AU"
    ]
)


# ============================================================
# FEATURE ENGINEERING
# ============================================================

if views > 0:

    engagement_rate = (
        (likes + comments) /
        views
    )

else:

    engagement_rate = 0


if video_length_minutes > 0:

    watch_time_per_minute = (
        watch_time_minutes /
        video_length_minutes
    )

else:

    watch_time_per_minute = 0


if subscribers > 0:

    views_per_subscriber = (
        views /
        subscribers
    )

else:

    views_per_subscriber = 0


# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame({

    "views": [
        views
    ],

    "likes": [
        likes
    ],

    "comments": [
        comments
    ],

    "watch_time_minutes": [
        watch_time_minutes
    ],

    "video_length_minutes": [
        video_length_minutes
    ],

    "subscribers": [
        subscribers
    ],

    "category": [
        category
    ],

    "device": [
        device
    ],

    "country": [
        country
    ],

    "engagement_rate": [
        engagement_rate
    ],

    "watch_time_per_minute": [
        watch_time_per_minute
    ],

    "views_per_subscriber": [
        views_per_subscriber
    ]
})


# ============================================================
# MAIN PAGE
# ============================================================

st.subheader("📋 Entered Video Information")

st.dataframe(
    input_data,
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

st.subheader("💰 Revenue Prediction")


if st.button(
    "Predict Ad Revenue",
    type="primary",
    use_container_width=True
):

    try:

        prediction = model.predict(
            input_data
        )

        predicted_revenue = prediction[0]

        st.success(
            "Prediction completed successfully!"
        )

        st.metric(
            label="Estimated Ad Revenue",
            value=f"${predicted_revenue:,.2f}"
        )

    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )


# ============================================================
# VIDEO METRICS
# ============================================================

st.divider()

st.subheader("📊 Video Performance")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Views",
        f"{views:,}"
    )


with col2:

    st.metric(
        "Likes",
        f"{likes:,}"
    )


with col3:

    st.metric(
        "Comments",
        f"{comments:,}"
    )


# ============================================================
# ENGAGEMENT METRICS
# ============================================================

st.subheader("📈 Calculated Engagement Metrics")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Engagement Rate",
        f"{engagement_rate:.2%}"
    )


with col2:

    st.metric(
        "Watch Time / Minute",
        f"{watch_time_per_minute:.2f}"
    )


with col3:

    st.metric(
        "Views / Subscriber",
        f"{views_per_subscriber:.2f}"
    )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.subheader("ℹ️ About the Project")

st.write(
    """
    Content Monetization Modeler is a machine learning
    project designed to predict YouTube advertising revenue.

    The project includes:

    • Data Cleaning

    • Exploratory Data Analysis

    • Feature Engineering

    • Missing Value Handling

    • Categorical Encoding

    • Regression Models

    • Model Evaluation

    • Revenue Prediction

    • Streamlit Application
    """
)


st.caption(
    "Content Monetization Modeler | "
    "Machine Learning Project"
)