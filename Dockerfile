# Dockerfile

FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r ml_model/requirements.txt
RUN pip install -r streamlit_app/requirements.txt

CMD ["streamlit", "run", "streamlit_app/app.py"]

