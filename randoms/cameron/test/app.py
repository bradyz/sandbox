from flask import Flask, render_template, request, url_for, redirect

from json import dumps


app = Flask(__name__)

number = 0


def some_logic(data):
    global number

    number += data


@app.route("/")
def api_root():
    global number

    return render_template("index.html", num=number)


# used by the get ajax call
@app.route("/number", methods=["GET"])
def api_get_number():
    global number

    return number


@app.route("/number", methods=["POST"])
def api_change_number_async():
    global number

    value = request.values.get('num', 0, type=int)
    print(value)
    some_logic(value)

    response = {
        "code": "success",
        "new_num": number
    }

    return dumps(response)


# should be a put but i cant figure out overrides without middleware
@app.route("/sync_number/", methods=["POST"])
def api_change_number_sync():
    global number

    value = int(request.form['the_input'])
    some_logic(value)

    return redirect(url_for('api_root'))

if __name__ == "__main__":
    app.run(debug=True)
