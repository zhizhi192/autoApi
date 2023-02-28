import logging
import os.path
import time
from logging import StreamHandler, FileHandler, Formatter

base_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(base_path, "log")
if not os.path.exists(log_path):
    os.mkdir(log_path)


class MyLogger:
    def __init__(self):
        self.log_name = os.path.join(log_path, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("api test log")
        self.logger.setLevel(logging.DEBUG)
        self.formatter = Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:%(message)s')
        self.streamHandler = StreamHandler()
        self.fileHandler = FileHandler(self.log_name, encoding='utf-8')
        self.streamHandler.setFormatter(self.formatter)
        self.fileHandler.setFormatter(self.formatter)
        self.logger.addHandler(self.streamHandler)
        self.logger.addHandler(self.fileHandler)

    def get_logger(self):
        return self.logger


logger = MyLogger().get_logger()
