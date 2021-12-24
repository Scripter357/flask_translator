from flask import Flask, render_template, request
import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "ef13e2c29cmsha4db27280354828p11d68fjsndf58f73edcbf"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


app = Flask(__name__)

my_words = {"hello": "привет", "Hello": "Привет", "no": "нет", "No": "Нет", "world": "мир", "World": "Мир"}

@app.route('/', methods=['GET', 'POST'])
def dict_page()
    if request.method == 'POST':
        word = request.form["word"]
	if mywords[word] == None:
           return render_template('result.html', word="This word isn't available.")
        return render_template('result.html', word=my_words[word])

    return render_template('dict.html')

if __name__ == '__main__':
    app.run(port=5002)

#method: GET
#url: 'https://google-translate1.p.rapidapi.com'/language/translate/v2/languages'
#accept-encoding: 'application/gzip'
#x-rapidapi-host: google-translate1.p.rapidapi.com
#x-rapidapi-key:

#SQLX 30 tasks -- homeword
#Install docker
