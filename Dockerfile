FROM python:3.8-slim

RUN apt-get update && apt-get install -y pkg-config libcairo2-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
