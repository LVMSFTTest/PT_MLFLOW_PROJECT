import streamlit as st
import pandas as pd
import mlflow.pyfunc

# Load the MLflow model
#model = mlflow.pyfunc.load_model("http://127.0.0.1:5000/#/experiments/0/runs/d94ed5e555614b0faea846186ed68abe/artifacts/model")
artifact_uri="http://127.0.0.1:5000/#/experiments/0/runs/d94ed5e555614b0faea846186ed68abe/model"
model = mlflow.pyfunc.load_model(artifact_uri)

st.title("Churn Analysis Prediction App")

# Upload CSV file through Streamlit
st.sidebar.header("Upload CSV Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the uploaded data
    st.sidebar.subheader("Uploaded Data:")
    st.sidebar.write(df)

    # Make predictions using the loaded model
    predictions = model.predict(df)

    # Display predictions
    st.subheader("Churn Predictions:")
    st.write(predictions)

else:
    st.warning("Upload a CSV file to get started.")