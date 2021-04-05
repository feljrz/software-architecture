import os
from os.path import dirname, join 
# from dotenv import load_dotenv

# env_path = join(dirname(__file__), '../.env')
# load_dotenv(env_path)
# DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_URL = os.environ["DATABASE_URL"]
# SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
# SQLALCHEMY_ECHO = True

DATABASE_URL="postgresql://postgres:12345678@172.20.0.6:5432/students_db"
SQLALCHEMY_DATABASE_URI="postgresql://postgres:12345678@172.20.0.6:5432/students_db"

