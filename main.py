from flask import Flask, render_template
from requests import get
from get_filedir import get_filepaths

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
    return render_template('course.html', courses=data)


@app.route("/about-us")
def about_us():
    return render_template('about-us.html')

@app.route("/courses/<id>")
def get_course(id):
    data = get(f"http://localhost:5000/course/{id}").json()
    if data:
        return render_template('individual-course.html', course = data)
    return "Course not found", 404

@app.route("/bursary")
def bursary():
    return render_template('bursary.html')

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=8000)