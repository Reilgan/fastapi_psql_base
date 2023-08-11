from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"


engine = create_engine(get_url(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)