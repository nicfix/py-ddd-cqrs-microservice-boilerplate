#!/bin/bash
alembic upgrade head

gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 pet_store.main:app
