from pymongo import MongoClient
import requests
import json_util
from flask import Flask, render_template, json, request, jsonify, Response

from csv import DictReader
from io import StringIO

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')
stockhist = MongoClient('mongodb://localhost:27017/')["bz"]["stockhistory"]


def json_load(data):
    return json.loads(data, object_hook=json_util.object_hook)


def json_dump(data):
    return json.dumps(data, default=json_util.default)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/stocks/', methods=['GET'])
def stocks():
    ticker = request.args.get('ticker', '')
    if ticker:
        query = list(stockhist.find({"ticker": ticker.upper()}).limit(10))
        if not query:
            query = get_info(ticker)
    else:
        query = list(stockhist.find({}).sort("_id", -1).limit(10))
    return Response(json_dump(query))


def get_info(ticker):
    site = "http://ichart.finance.yahoo.com/table.csv?s=" + ticker
    query = DictReader(StringIO(requests.get(site).text))
    queries = []
    for q in query:
        q["ticker"] = ticker.upper()
        queries.append(q)
    if queries:
        stockhist.insert_many(queries)
    return list(stockhist.find({"ticker": ticker.upper()}).limit(10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
