# """"
# This class provides functionality related to how we perform the OCR for ID card types.
# 1. MRZ code enabled. (Passport etc)
# 2. Country specific ID card and social security cards, each having a standard and unique template and language.
#     example: India:AdhaarCard:English+StateLanguage.
# """
#
# import cv2
# import pytesseract
# from pytesseract import Output
#
# # pytesseract config:
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# languages = ["eng", "script/Devanagri"]  # English and French
#
#
# # Load the image using OpenCV
# image = cv2.imread("C:/Users/deedsingh/PycharmProjects/id-scan/samples/IN/passport-front.jpg")
#
#
#
# # Convert the image to grayscale (recommended for OCR)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Use Pytesseract to extract text from the image
# extracted_text = pytesseract.image_to_string(gray_image,lang=languages, config="--psm 6", output_type=Output.STRING)
#
# # Print the extracted text
# print(extracted_text)
