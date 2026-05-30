FROM python:3.12-slim

COPY ./ /src/
WORKDIR /src
RUN pip install -r requirements.txt
