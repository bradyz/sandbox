from flask import Flask, render_template, request, url_for, redirect

import requests
from json import dumps


app = Flask(__name__)

app.config.from_object("config")


@app.route("/")
def api_root():
    return render_template("index.html")


@app.route("/submit/", methods=["POST"])
def api_submit_question():
    code = request.form["code"]
    test_cases = [request.form["test case"]]
    lang = 5
    headers = {'Content-Type': 'application/json'}

    payload = {"source": code,
               "api_key": app.config["HR_KEY"],
               "lang": lang,
               "testcases": test_cases}
    print(payload)
    print(app.config["HR_URL"])

    response = requests.post(app.config["HR_URL"], data=payload, headers=headers)
    print(response.status_code)
    response = requests.post(app.config["HR_URL"], json=dumps(payload), headers=headers)
    print(response.status_code)

    return redirect(url_for('api_root'))

if __name__ == "__main__":
    app.run(debug=True)
