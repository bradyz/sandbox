from pymongo import MongoClient
import requests
import json_util
from flask import Flask, render_template, json, request, jsonify

from csv import DictReader
from StringIO import StringIO

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
    print(ticker)
    if ticker:
        print("a")
        query = list(stockhist.find({"ticker": ticker.upper()}).limit(10))
        if not query:
            query = get_info(ticker)
    else:
        print("b")
        query = list(stockhist.find().limit(10))
    return json_dump(query)


def get_info(ticker):
    site = "http://ichart.finance.yahoo.com/table.csv?s=" + ticker
    print(site)
    query = DictReader(StringIO(requests.get(site).content))
    queries = []
    for q in query:
        q["ticker"] = ticker.upper()
        queries.append(q)
    stockhist.insert_many(queries)
    return list(stockhist.find({"ticker": ticker.upper()}).limit(10))


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
