FROM python:3.8-alpine

RUN adduser -D wplt

RUN mkdir -p /wplt/app
WORKDIR /wplt

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY app/. app/
COPY config.py WPLT.py ./

ENV FLASK_APP WPLT.py
ENV FLASK_ENV production

RUN chown -R wplt:wplt ./
USER wplt

EXPOSE 5000

CMD flask run --host 0.0.0.0
