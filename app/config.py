import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ['DATABASE_HOST']
DB_PORT = os.environ['DATABASE_PORT']
DB_USER = os.environ['DATABASE_USERNAME']
DB_NAME = os.environ['DATABASE_NAME']
DB_PASS = os.environ['DATABASE_PASSWORD']
SECRET_AUTH = os.environ['SECRET_AUTH']
