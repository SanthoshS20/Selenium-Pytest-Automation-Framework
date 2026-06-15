import os
from datetime import datetime

# Base directory for the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

# Logging configuration
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True) # "Do not throw an error if the folder already exists."
LOG_FILE_NAME = f"automation_{TIMESTAMP}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)

# Screenshots configuration
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Test data
TEST_DATA_PATH = os.path.join(BASE_DIR, 'test_data')
BOOKINGS_DATA_FILE_PATH = os.path.join(TEST_DATA_PATH, 'bookings_data.json')
EVENTS_DATA_FILE_PATH = os.path.join(TEST_DATA_PATH, 'event_data.json')