import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        log_file_path = os.path.join(os.path.abspath(os.curdir), logs_dir, 'automation.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Create a file handler and set the formatter
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        return logger
