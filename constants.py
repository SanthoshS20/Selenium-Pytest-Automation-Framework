import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# "Do not throw an error if the folder already exists."
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE_NAME = f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)
LOG_LEVEL = 'INFO'