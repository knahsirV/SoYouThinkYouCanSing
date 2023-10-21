from flask import Flask, request

from google.cloud import storage

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


import os

ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_mp3():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and allowed_file(file.filename):
        print("File is valid")

        # TODO - create filenames that are unique for users
        print(file.filename)
        storage_client = storage.Client()
        bucket = storage_client.bucket('sytycs')
        blob = bucket.blob(file.filename)

        blob.upload_from_filename(file.filename)
        
        return "File uploaded successfully"

    return "Invalid file format. Please upload an MP3 file."

# get a song from the database
@app.route('/get_song', methods=['GET'])
def get_song():
    # song_name = request.args.get('song_name')
    song_name = request.args.get('song_name')
    print(song_name)
    storage_client = storage.Client()
    bucket = storage_client.bucket('sytycs')
    blob = bucket.blob(song_name)
    blob.download_to_filename('downloaded_online' + song_name)
    return "Song downloaded successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))