import json
from flask import Flask

with open('tests/courses_data.json', 'r') as file:
    courses_data = json.load(file)

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, World!"


@app.route("/courses")
def courses():
    return courses_data


if __name__ == "__main__":
    app.run(debug=True)
