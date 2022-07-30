#!/bin/bash
# This is a development entry point, do not use it in production
python run.py migrate_database

uvicorn pet_store.main:app