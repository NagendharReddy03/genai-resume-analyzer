import os
from pathlib import Path

# Load .env file if present
from dotenv import load_dotenv
load_dotenv()

BASEDIR = Path(__file__).parent.resolve()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASEDIR}/instance/site.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
