FROM python:3.9.7-slim


ENV PYTHONUNBUFFERED 1



WORKDIR /app

COPY . /app
RUN pip install -e .

EXPOSE 3000