import logging, constants


class Utilities:

    def __init__(self, logger_name, log_level):
        self.logger_name = logger_name
        self.log_level = log_level

    def get_logger(self):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.log_level)
        log_format = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s')
        file_handler = logging.FileHandler(constants.LOG_FILE_PATH)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
        return logger
