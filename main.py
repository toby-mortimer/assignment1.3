from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
<<<<<<< HEAD
def base():
    return render_template("base.html")
=======
def index():
    return render_template('index.html')
>>>>>>> fd9683bd5260ef7021609cc81dca475a1d934f86

@app.route("/courses")
def courses():
    return render_template('course.html')

if __name__ == '__main__':
    app.run(debug=True)