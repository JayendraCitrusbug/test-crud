from sqlalchemy.orm import Session
import os
import redis
from contextlib import contextmanager

# You may need to adjust this import based on where SessionLocal is defined
from src.domain.models import SessionLocal

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

@contextmanager
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_redis():
    r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    try:
        yield r
    finally:
        r.close() 