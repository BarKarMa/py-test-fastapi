FROM python:3.9.7-slim


ENV PYTHONUNBUFFERED 1 

WORKDIR /app

EXPOSE 8000

COPY . /app
RUN pip install -e .