import pymongo
import requests
import json_util
from flask import Flask, render_template, json, request

from csv import DictReader
from StringIO import StringIO
from collections import namedtuple

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')
stockhist = pymongo.Connection('localhost', 27017)['bz']['stockhistory']


def json_load(data):
    return json.loads(data, object_hook=json_util.object_hook)


def json_dump(data):
    return json.dumps(data, default=json_util.default)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/stocks', methods=['GET'])
def func1():
    return stocks("aapl")


@app.route('/stocks/<ticker>', methods=['GET'])
def stocks(ticker):
    fn = ("Date", "Open", "High", "Low", "Close", "Volume", "Adj")
    query = list(stockhist.find().limit(1))
    if not query:
        site = "http://ichart.finance.yahoo.com/table.csv?s=" + ticker
        reader = DictReader(StringIO(requests.get(site).content))
        Data = namedtuple('Data', fn[1:])
        query = {"ticker": ticker, "data": []}
        for r in reader:
            print(r.values())
            query["data"].append(Data(*r.values()[1:]))
        stockhist.save(query)
    print(json_dump(query))
    return json_dump(query)

# @app.route('/todos')
# def list_todos():
#     return json_dump(list(todos.find()))
#
#
# @app.route('/todos',  methods=['POST'])
# def new_todo():
#     todo = json_load(request.data)
#     todos.save(todo)
#     return json_dump(todo)
#
#
# @app.route('/todos/<todo_id>', methods=['PUT'])
# def update_todo(todo_id):
#     todo = json_load(request.data)
#     todos.save(todo)
#     return json_dump(todo)
#
#
# @app.route('/todos/<todo_id>', methods=['DELETE'])
# def delete_todo(todo_id):
#     todos.remove(ObjectId(todo_id))
#     return ""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
