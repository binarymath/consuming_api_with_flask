from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
url = "https://openai80.p.rapidapi.com/images/generations"

payload = {
    "prompt": "desenho de super-heroi",
    "n": 1,
    "size": "1024x1024"
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
    "X-RapidAPI-Host": os.environ['X-RapidAPI-Host']
}


@app.route('/')
def index():
    # Make API request to RapidAPI
    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()  # assuming the response is in JSON format
    return render_template('index.html', data=data)


response1 = requests.request("POST", url, json=payload, headers=headers)

print(response1.text)

if __name__ == '__main__':
    app.run()
