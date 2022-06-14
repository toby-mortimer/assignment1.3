from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/courses")
def courses():
    return render_template('course.html')

if __name__ == '__main__':
    app.run(debug=True)