from flask import Flask, render_template, jsonify, request
from stock_scraper import get_data

import requests

giphy_key = "dc6zaTOxFJmzC"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    return jsonify(get_data())


@app.route("/gifs", methods=['GET'])
def gifs():
    response = requests.get("http://api.giphy.com/v1/gifs/random?api_key="
                            + giphy_key)
    gif_url = response.json()['data']['image_url']

    return render_template("gifs.html", gif=gif_url)

if __name__ == "__main__":
    app.run(debug=True)
