import logging


class Logger:
    def __init__(self, level=logging.INFO):
        logging.basicConfig(
            level=level,
            format="(%(asctime)s) [%(levelname)s]: %(message)s",
            filename="tool.log",
            filemode="w",
        )
        self.logger = logging.getLogger()

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
