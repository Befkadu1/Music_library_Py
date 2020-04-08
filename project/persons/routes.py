from flask import Flask, request, url_for, Blueprint, jsonify
from project.models import Person, persons_schema, person_schema
from project import db

persons_blueprint = Blueprint('persons', __name__, template_folder='template')

# endpoint to create new person
@persons_blueprint.route("", methods=["POST"])
def add_person():
    full_name = request.json['full_name']
    age = request.json['age']

    new_person = Person(full_name, age)
    db.session.add(new_person)
    db.session.commit()
   
    return person_schema.jsonify(new_person) 

# endpoint to show all persons
@persons_blueprint.route("/", methods=["GET"])
def get_persons():
    all_persons = Person.query.all()
    result = persons_schema.dump(all_persons)
    return jsonify(result)

# endpoint to get person detail by id
@persons_blueprint.route("/<id>", methods=["GET"])
def person_detail(id):
    person = Person.query.get(id)
    return person_schema.jsonify(person)

# endpoint to update person
@persons_blueprint.route("/<id>", methods=["PUT"])
def person_update(id):
    person = Person.query.get(id)
    full_name = request.json['full_name']
    age = request.json['age']

    person.age = age
    person.full_name = full_name

    db.session.commit()
    return person_schema.jsonify(person)


# endpoint to delete person
@persons_blueprint.route("/<id>", methods=["DELETE"])
def person_delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()

    return person_schema.jsonify(person)
