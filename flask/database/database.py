from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from .settings import DATABASE_URL
from models import models

print(DATABASE_URL)
engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import models #Otherwise we neet to import them before calling init_db()
    # Database
    
    Base.metadata.create_all(bind=engine)
