import requests

# url = "http://127.0.0.1:5000/upload"
# file = {'file': open('audio1.wav', 'rb')}

# response = requests.post(url, files=file)
url = "http://127.0.0.1:5000/get_song?song_name=audio1.wav"
response = requests.get(url)

print(response.text)
