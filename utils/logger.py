import logging, constants


class Logger:

    @staticmethod   
    def get_logger(logger_name, log_level):
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        log_format = logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s')
        file_handler = logging.FileHandler(constants.LOG_FILE_PATH)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
        return logger
