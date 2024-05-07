from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
LOG_LEVEL = int(os.getenv("LOG_LEVEL", 1))
