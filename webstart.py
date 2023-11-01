import os
from flask import Flask, request, jsonify
from ocr.mrz import MRZ

app = Flask("OCR APP")

# Define the directory where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/mrz', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    if 'key' not in request.files:
        return jsonify({'error': 'Please enter key and try again, enter valid key'})

    file = request.files['image']
    key = request.

    if not validate(key):
        return jsonify({'error': 'Not authorized, enter valid key'})

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the uploaded image to the server
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Pass the image path to a function that processes it
        process_image(filename)
        handler = MRZ()
        handler.start_process(filename)
        out = handler.get_string()
        print(out)


        # Delete the uploaded image
        os.remove(filename)

        return jsonify(out)

@app.route('/', methods=['GET'])
def health():
    return jsonify({'Success': 'I am alive!'})

def process_image(image_path):
    # Add your image processing logic here
    print(f"Processing image at path: {image_path}")

def validate(key):
    return "e7e04bcf8df2311e89301724070af403f1eb2fede1d0aa79f50e96cabfbc7e5f" == key

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
