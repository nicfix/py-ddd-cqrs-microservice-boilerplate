FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
    && rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

RUN useradd -ms /bin/bash app
USER app

ENTRYPOINT ["sh", "entrypoint.sh"]

