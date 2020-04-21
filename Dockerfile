FROM python:3.8-alpine

RUN mkdir -p /wplt/app
WORKDIR /wplt

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/* ./app/
COPY config.py .flaskenv WPLT.py ./

EXPOSE 5000