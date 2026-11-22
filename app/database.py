# database.py এর কাজ একটাই: Python কোডকে MySQL এর সঙ্গে সংযুক্ত করা।


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# ১. Create SQLAlchemy engine From DATABASE_URL
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True  
    
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()