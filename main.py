from flask import Flask, render_template
from requests import request

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

@app.route("/applied-science")
def applied():

    return render_template('applied.html', description="")



if __name__ == '__main__':
    app.run(debug=True)
