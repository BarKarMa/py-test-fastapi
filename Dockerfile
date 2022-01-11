FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1

<<<<<<< HEAD

=======
>>>>>>> f130efcae925874042a2168b435e1e1a2cfab4f2
EXPOSE 8000

WORKDIR /app

<<<<<<< HEAD
COPY . /app

RUN pip install -e .
=======

COPY . /app
RUN pip install -e .

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]
>>>>>>> f130efcae925874042a2168b435e1e1a2cfab4f2
