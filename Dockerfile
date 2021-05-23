FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY pet_store /usr/src/app/pet_store

CMD ["uvicorn", "pet_store.entrypoints.api:app", "--host", "0.0.0.0", "--port", "8080"]

