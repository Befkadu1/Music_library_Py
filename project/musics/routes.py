from flask import Flask, request, url_for, Blueprint, jsonify
from project.models import Music, musics_schema, music_schema
from project import db

musics_blueprint = Blueprint('musics', __name__, template_folder='template')

# endpoint to show all musics
@musics_blueprint.route("/", methods=["GET"])
def get_musics():
    all_musics = Music.query.all()
    result = musics_schema.dump(all_musics)
    return jsonify(result)

# endpoint to get a music for selected person
@musics_blueprint.route("/person/<person_id>", methods=["GET"])
def get_musics_for_person(person_id):
    
    musics = Music.query.all()
    result = musics_schema.dump(musics)
    # for music in result:
    #     if str(music['person_id']) == person_id:
    #         return jsonify(result)
    #     else: return jsonify([])
    return jsonify([music for music in result if str(music['person_id']) == person_id])

# endpoint to create new music
@musics_blueprint.route("", methods=["POST"])
def add_music():
    title = request.json['title']
    person_id = request.json['person_id']

    new_music = Music(title, person_id)
    db.session.add(new_music)
    db.session.commit()
   
    return music_schema.jsonify(new_music) 

# endpoint to get music detail by id
@musics_blueprint.route("<id>", methods=["GET"])
def get_music(id):

    music = Music.query.get(id)
    return music_schema.jsonify(music)

# endpoint to update music detail by id
@musics_blueprint.route("/<id>", methods=["PUT"])
def update_music(id):

    music = Music.query.get(id)
    title = request.json["title"]

    music.title = title
    db.session.commit()

    return music_schema.jsonify(music)

# endpoint to delete music 
@musics_blueprint.route("/<id>", methods=["DELETE"])
def delete_music(id):

    music = Music.query.get(id)
    db.session.delete(music)
    db.session.commit()

    return music_schema.jsonify(music)

