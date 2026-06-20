import logging, constants
from config.config_manager import ConfigManager
from concurrent_log_handler import ConcurrentRotatingFileHandler

class Logger:

    @staticmethod   
    def get_logger(logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(ConfigManager.get("log_level"))
        if not logger.handlers:
            logger.propagate = False
            log_format = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s')
            file_handler = ConcurrentRotatingFileHandler(
                constants.LOG_FILE_PATH,
                maxBytes=10_000_000,
                backupCount=5
            )
            file_handler.setFormatter(log_format)
            logger.addHandler(file_handler)
        return logger
