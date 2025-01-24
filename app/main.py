from fastapi import FastAPI
from app.routes import user as user_routes
from app.database import Base, engine
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Access environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")


# Initialize the FastAPI app
app = FastAPI()

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Include user routes
app.include_router(user_routes.router)