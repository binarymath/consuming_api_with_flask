from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)


@app.route('/')
def formpage():
    return render_template('index.html')


@app.route('/image', methods=['POST'])
def processform():
    type_figure = request.form['type_figure']

    url = "https://openai80.p.rapidapi.com/chat/completions"

    payload = {"prompt": type_figure,
               "n": 1,
               "size": "1024x1024"}

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
        "X-RapidAPI-Host": os.environ['X-RapidAPI-Host']
    }
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
