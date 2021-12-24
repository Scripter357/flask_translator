from flask import Flask, render_template, request
import requests
import sys

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': ""
    }


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        payload = "source=en&target=ru&format=text&q="+word
        response = requests.request("POST", url, data=payload, headers=headers)
        text = response.text.split(':')[3].split('}')[0]
        return render_template('result.html', word=text)

    return render_template('dict.html')

if __name__ == '__main__':
    app.run(port=5002)
