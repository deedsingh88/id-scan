""""
OCR for just passport, input passport image file and output is json with details
"""
from passporteye import read_mrz
import pytesseract
from PIL import Image
import json
import configparser


class MRZ:

    def __init__(self):
        self.text = None

    def start_process(self, image_path):

        if self.__validate__(image_path):
            mrz_data = read_passport_mrz(image_path)
            if mrz_data:
                print("MRZ Data:")
                print(mrz_data)
                dict_data = dict(mrz_data)
                jsondata = json.dumps(dict_data)
                self.text = jsondata
            else:
                print("MRZ data not found.")
        pass

    def get_string(self):
        if self.text:
            return self.text
        else:
            print("Processing not started, please call the start_process method")

    def __validate__(self, image_path):
        try:
            Image.open(image_path)
            return True
        except OSError as e:
            print(f"Image loading failed: {e}")
            return False


def read_passport_mrz(image):
    mrz = read_mrz(image)

    if mrz is not None:
        return mrz.to_dict()
    else:
        return None


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read("../config.ini")
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

    # Example usage:
    handler = MRZ()
    image_path = "C:/Users/deedsingh/PycharmProjects/id-scan/samples/TN/resident-card.jpg"
    handler.start_process(image_path)
    out = handler.get_string()
    print(out)

    # # image_path = "C:/Users/deedsingh/PycharmProjects/id-scan/samples/IN/passport-front.jpg"
    # image_path = "C:/Users/deedsingh/PycharmProjects/id-scan/samples/TN/resident-card.jpg"
    # mrz_data = read_passport_mrz(image_path)
    # if mrz_data:
    #     print("MRZ Data:")
    #     print(mrz_data)
    #     dict_data = dict(mrz_data)
    #     json = json.dumps(dict_data)
    #     print(json)
    # else:
    #     print("MRZ data not found.")
