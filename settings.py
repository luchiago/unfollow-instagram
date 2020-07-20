import os

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
NUMBER = os.getenv("IG_NUMBER")
TWO_FACTOR = os.getenv("TWO_FACTOR")
USERNAMES_FILENAME = os.getenv("USERNAMES_FILENAME")
