from flask import Flask, render_template
from requests import get

app = Flask(__name__, )

# def prepare_courses_data(data):
#     result = []
#     for element in data:
#         element = 
#         result.append(element)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/courses")
def courses():
    data = get("http://localhost:5000/course").json()
    return render_template('course.html', courses = data)

@app.route("/about-us")
def about_us():
    return render_template('about-us.html')

@app.route("/applied-science")
def applied():
    return render_template('applied.html', description="")

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=8000)
