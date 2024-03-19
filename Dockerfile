# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install Python dependencies for Streamlit app and ML model
RUN pip install --no-cache-dir -r streamlit_app/requirements.txt \
    && pip install --no-cache-dir -r ml_model/requirements.txt


# Expose the port the app runs on
EXPOSE 8501

# Define environment variable
ENV PORT=8501

# Run app.py when the container launches
CMD ["streamlit", "run", "streamlit_app/app_monitor.py"]
