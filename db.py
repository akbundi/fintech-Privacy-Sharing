from sqlalchemy import create_engine, Column, String, Float, JSON, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+asyncmy://root@localhost:3306/fintech")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True)
    name = Column(String)
    bank_account = Column(String)
    income = Column(Float)
    transaction_history = Column(JSON)
    pii = Column(JSON)
    device_data = Column(JSON)

class Consent(Base):
    __tablename__ = 'consents'
    user_id = Column(String, primary_key=True)
    allowed_fields = Column(JSON)
    expiration = Column(String)

Base.metadata.create_all(bind=engine)