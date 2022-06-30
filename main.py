from flask import Flask, render_template
from requests import get
<<<<<<< HEAD
=======
from get_filedir import get_filepaths
>>>>>>> 137da6a19e2c3aa2283fb61805939e86b64a0d80

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
    course_images = get_filepaths("static/images")
    data = get("http://localhost:5000/course").json()
    return render_template('course.html', courses = data, images = course_images)

@app.route("/about-us")
def about_us():
    return render_template('about-us.html')


@app.route("/courses/applied-science")
def applied():
<<<<<<< HEAD
    course = get("http://localhost:5000/course/2").json()
    return render_template('applied.html', description=course["descriptions"])


@app.route("/bursary")
def bursary():
    return render_template

=======
    return render_template('applied.html', description="")
>>>>>>> 137da6a19e2c3aa2283fb61805939e86b64a0d80

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=8000)
