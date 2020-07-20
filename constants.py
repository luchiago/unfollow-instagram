import os

from selenium import webdriver

from settings import USERNAMES_FILENAME

BASE_URL = "https://www.instagram.com"
BROWSER = webdriver.Firefox()
BASE_DIR = os.getcwd()
FILE = USERNAMES_FILENAME + ".txt"
FILE_LOCATION = os.path.join(BASE_DIR, FILE)
