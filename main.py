from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/courses")
def courses():
    return render_template('course.html')


@app.route("/aboutus")
def about_us():
    return render_template('about-us.html')

@app.route("/carousel")
def carousel():
    return render_template('carousel-test.html')


if __name__ == '__main__':
    app.run(debug=True)
