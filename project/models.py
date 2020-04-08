# import from the __init__ file
from project import db, ma

# declare Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

# This part defined structure of response of our endpoint. JSON response
class PersonSchema(ma.Schema):
    class Meta:
        # JSON response will have two keys(full_name, and age)
        fields = ('id', 'full_name', 'age')

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

########################################################declare Music model ###############################################
class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
    person = db.relationship("Person", backref="musics")

    def __init__(self, title, person_id):
        self.title = title
        self.person_id = person_id

# This part defined structure of response of our endpoint. JSON response
class MusicSchema(ma.Schema):
    class Meta:
        # JSON response will have two keys(full_name, and age)
        fields = ('id', 'title', 'person_id')

music_schema = MusicSchema()
musics_schema = MusicSchema(many=True)