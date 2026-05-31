import json
from utils.logger import Logger

class JSONReader:

    logger = Logger.get_logger(__name__)

    @staticmethod
    def read_json_data_from_file(file_path):
        try:
            JSONReader.logger.info(f"Reading JSON data from file: {file_path}")
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            return json_data
        except FileNotFoundError:
            raise FileNotFoundError(f"file not found: {file_path}")
        except Exception as err:
            raise Exception(f"An error occurred while reading JSON data: {err}")
