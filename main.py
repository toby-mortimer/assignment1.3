from flask import Flask, render_template
from requests import get

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/courses")
def courses():
    return render_template('course.html')


@app.route("/about-us")
def about_us():
    return render_template('about-us.html')


@app.route("/courses/applied-science")
def applied():
    course = get("http://localhost:5000/course/2").json()
    return render_template('applied.html', description=course["descriptions"])


@app.route("/bursary")
def bursary():
    return render_template


if __name__ == '__main__':
    app.run(debug=True)
