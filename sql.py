import re
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# init flask app
app = Flask(__name__)

# get the directory of our app
basedir = os.path.abspath(os.path.dirname(__file__))
# set the path to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'db.sqlite'
# required to stop some warnings in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# init SQL Alchemy
db = SQLAlchemy(app)
# init Marshmallow
ma = Marshmallow(app)

# creates the database model for the table


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    type = db.Column(db.String(100))
    teacher_info = db.Column(db.String(100))
    requirements = db.Column(db.String(100))
    ucas_points = db.Column(db.String(100))
    topics = db.Column(db.String(100))
    description = db.Column(db.String(500))
    testimonials = db.Column(db.String(500))
    exam_details = db.Column(db.String(100))

    def __init__(self, title, type, teacherinfo, requirements, ucaspoints, topics, description, testimonials, examdetails):
        self.title = title
        self.type = type
        self.teacher_info = teacherinfo
        self.requirements = requirements
        self.ucas_points = ucaspoints
        self.topics = topics
        self.description = description
        self.testimonials = testimonials
        self.exam_details = examdetails

# creates the schema for marshmallow to use


class CoursesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'type', 'teacher_info', 'requirements',
                  'ucas_points', 'topics', 'description', 'testimonials', 'exam_details')


# creates an instance of the schema
course_schema = CoursesSchema()  # single info
Mcourse_schema = CoursesSchema(many=True)  # many info

# C.R.U.D. operations for API
# Creates a new person in the databse


@app.route('/course', methods=['POST'])
def add_course():
    title = request.json['title']
    type = request.json['type']
    teacher_info = request.json['teacher_info']
    requirements = request.json['requirements']
    ucas_points = request.json['ucas_points']
    topics = request.json['topics']
    description = request.json['description']
    testimonials = request.json['testimonials']
    exam_details = request.json['exam_details']

    new_course = Courses(title, type, teacher_info, requirements,
                         ucas_points, topics, description, testimonials, exam_details)
    db.session.add(new_course)
    db.session.commit()

    return course_schema.jsonify(new_course)


# Gets all people in the database
@app.route('/course', methods=['GET'])
def get_course():
    all_course = Courses.query.all()
    result = course_schema.dump(all_course)
    return jsonify(result)


# Gets a single person by ID
@app.route('/course/<id>', methods=['GET'])
def get_person(id):
    course = Courses.query.get(id)
    return course_schema.jsonify(course)


# Updates a person with the id
@app.route('/course/<id>', methods=['PUT'])
def update_course(id):
    course = Courses.query.get(id)
    title = request.json['title']
    type = request.json['type']
    teacherinfo = request.json['teacher_info']
    requirements = request.json['requirements']
    ucaspoints = request.json['ucas_points']
    topics = request.json['topics']
    description = request.json['description']
    testimonials = request.json['testimonials']
    examdetails = request.json['exam_details']

    course.title = title
    course.type = type
    course.teacher_info = teacherinfo
    course.requirements = requirements
    course.ucas_points = ucaspoints
    course.topics = topics
    course.description = description
    course.testimonials = testimonials
    course.exam_details = examdetails

    db.session.commit()
    return course.jsonify(course)


# Deletes the person with the id
@app.route('/course/<id>', methods=['DELETE'])
def delete_course(id):
    course = Courses.query.get(id)
    db.session.delete(course)
    db.session.commit()
    return course_schema.jsonify(course)


# Main program loop
if __name__ == '__main__':
    app.run(debug=True)
