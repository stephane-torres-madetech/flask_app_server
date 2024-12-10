from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, World!'

@app.route('/courses')
def courses():
  return "<h1>Courses</h1><ul><li>Course 1</li><li>Course 2</li><li>Course 3</li><li>Course 4</li></ul>"

if __name__ == '__main__':
    app.run(debug=True)