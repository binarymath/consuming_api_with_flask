from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

type_figure = "computer"
size = "1024x1024"

app = Flask(__name__)
url = "https://openai80.p.rapidapi.com/images/generations"

payload = {
    "prompt": type_figure,
    "n": 1,
    "size": size
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


if __name__ == '__main__':
    app.run()
