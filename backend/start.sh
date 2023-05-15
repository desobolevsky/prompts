#!/bin/bash

# Check if the migrations have already been applied
if [ ! -f alembic/versions/$(poetry run alembic current | awk '{print $4}') ]; then
    echo "Upgrading database with Alembic"
    poetry run alembic upgrade head

    # initialize db with some dummy data
    poetry run python init_db.py
fi

poetry run uvicorn main:app --host 0.0.0.0 --port 8000
