import configparser
from abc import abstractmethod


class OCRHandle:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    @abstractmethod
    def start_process(self, image):
        pass

    @abstractmethod
    def get_string(self):
        pass

    @abstractmethod
    def __validate__(self,image_path):
        pass

    def destroy(self):
        self.config = None

    def read_config(self):
        return self.config
