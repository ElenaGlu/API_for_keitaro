import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

URL_AFF_NETWORK = os.getenv('URL_AFF_NETWORK')
URL_OFFER = os.getenv('URL_OFFER')
KEY_K = os.getenv('KEY_K')
