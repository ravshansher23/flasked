FROM python:3.10.11-buster

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN apt-get update && apt-get install -y libpq-dev build-essential


RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5000

ENTRYPOINT flask run --host 0.0.0.0

CMD [ "flask", "run" ]

