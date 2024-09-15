FROM python:3.10.15-slim-bullseye

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt