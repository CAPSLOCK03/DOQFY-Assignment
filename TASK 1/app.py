from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    url = request.form['url']
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return render_template('index.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)
