FROM python:3.8-slim-buster
# This is a development docker file, do not use it in production
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
# you are supposed to mount the app folder in the run stage,
# no code from the app is copied here.
COPY entrypoint.sh ./
EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]

