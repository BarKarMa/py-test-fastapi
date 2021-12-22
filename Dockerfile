FROM python:3.9.7-slim


ENV PYTHONUNBUFFERED 1

EXPOSE 7001

WORKDIR /app

COPY . /app
RUN pip install -e .

