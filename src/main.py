"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planets, Charachters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/people', methods=['GET'])
def handle_hello():

    # singleid = list(map(lambda x: x.serialize(), singleperson))
    people = People.query.all()
    # serialize is a function in your models that your importing to be able to get the email and id back, remember how to use lambda,
    # there is documentation for lambda in your projects
    people_list = list(map(lambda x: x.serialize(), people))
    # jsonify takes the function and reads it in json
    return jsonify(people_list), 200

# we use int:people id to make it so you can use the number thats read there in postman at the end of the url, the id


@app.route('/people/<int:people_id>', methods=['GET'])
def persons_id(people_id):

    singleperson = People.query.get(people_id)
    print("This is the position of a single person: ", singleperson)
    return jsonify(singleperson.serialize())


@app.route('/people', methods=['POST'])
def create_people():
    request_body = request.get_json()
    new_people = People(
        email=request_body['email'], password=request_body['password'], is_active=request_body['is_active'])
    db.session.add(new_people)
    db.session.commit()
    return f"the new user {request_body['email']} was created succesfully", 200


@app.route('/planets', methods=['GET'])
def planets():
    planets = Planets.query.all()
    planets_list = list(map(lambda i: i.serialize(), planets))
    return jsonify(planets_list), 200


@app.route('/planets/<int:planets_id>', methods=['GET'])
def planetsId(planets_id):
    singlePlanet = Planets.query.get(planets_id)
    print("this is the position of a single person: ", singlePlanet)
    return jsonify(singlePlanet.serialize())


@app.route('/planets', methods=['POST'])
def create_planets():
    request_body = request.get_json()
    new_planets = Planets(
        planet_name=request_body['planet_name'], rotation_speed=request_body['rotation_speed'])
    db.session.add(new_planets)
    db.session.commit()
    return f"the new planet {request_body['planet_name']} was created succesfully", 200


@app.route('/charachters', methods=['GET'])
def charachters():

    charachters = Charachters.query.all()
    charachters_list = list(map(lambda i: i.serialize(), charachters))
    return jsonify(charachters_list), 200


@app.route('/<int:charachters_id>', methods=['GET'])
def charachtersId(charachters_id):
    singlecharachter = Charachters.query.get(charachters_id)
    print("this is the position of a single charachter: ", singlecharachter)
    return jsonify(singlecharachter.serialize())


@app.route('/charachters', methods=['POST'])
def create_charachters():
    request_body = request.get_json()
    new_charachters = Charachters(charachters_name=request_body['charachters_name'], home_planet=request_body['home_planet'],
                                  persons_age=request_body['persons_age'], persons_species=request_body['persons_species'])
    db.session.add(new_charachters)
    db.session.commit()
    return f"the new charachter {request_body['charachters_name']} was created succesfully", 200

#     class Request(db.Model):
#     __tablename__ = 'request'
#     id = db.Column(db.Integer, primary_key=True)
#     applicationdate = db.Column(db.DateTime)

# class Agent(db.Model):
#     __tablename__ = 'agent'
#     id = db.Column(db.Integer, primary_key=True)
#     request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
#     request = db.relationship("Request", backref=backref("request", uselist=False))

#     name = db.Column(db.String(80))
#     company = db.Column(db.String(80))
#     address = db.Column(db.String(180))
# Now you can access your models like this:

# request = Request.query.first()
# print(request.agent.name)

# agent = Agent.query.first()
# print(agent.request.applicationdate)


# dont do favourites, have users planets and people, and use the data modeling in the website

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
