from flask import Flask, render_template, request, url_for, redirect

import requests
import json


app = Flask(__name__)

app.config.from_object("config")


@app.route("/")
def api_root(message=None):
    return render_template("index.html", msg=message)


@app.route("/submit/", methods=["POST"])
def api_submit_question():
    code = request.form["code"]
    test_cases = [request.form["test case"]]
    lang = 5

    payload = {"source": code,
               "api_key": app.config["HR_KEY"],
               "lang": lang,
               "testcases": json.dumps(test_cases)}

    try:
        response = requests.post(app.config["HR_URL"], data=payload)
        res_json = json.loads(response.text)
        msg = res_json["result"]["message"][0]
    except Exception as e:
        msg = "Exception - check console"
        print(e)

    return api_root(msg)

if __name__ == "__main__":
    app.run(debug=True)
