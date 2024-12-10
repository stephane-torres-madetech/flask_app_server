import json
from flask import Flask
from tests import courses_data

course_data = courses_data.course_data


app = Flask(__name__)

@app.route("/")
def index():
    return "hello, World!"


@app.route("/courses")
def courses():
    return json.dumps(course_data)


if __name__ == "__main__":
    app.run(debug=True)
