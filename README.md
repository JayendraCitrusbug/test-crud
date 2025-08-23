# test-crud

A simple FastAPI project with CRUD APIs for voice assessments.

## Features

- Voice assessment routes (CRUD)
- DB service layer
- Redis integration

## Tech Stack

- Python
- FastAPI
- Redis
- Uvicorn

## Run Locally

```bash
git clone git@github.com:JayendraCitrusbug/test-crud.git
cd test-crud
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Make sure Redis is running locally or update config accordingly.

## API Docs

[http://localhost:8000/docs](http://localhost:8000/docs)
