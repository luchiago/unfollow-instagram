import os

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TWO_FACTOR = os.getenv("TWO_FACTOR")
USERNAMES_FILE = os.getenv("USERNAMES_FILE")
