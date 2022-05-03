from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)

    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# So we had to copy and paste the top portion and change some things to make the planets get


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_speed = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name,
            "rotationSpeed": self.rotation_speed
            # do not serialize the password, its a security breach
        }

        # WHEN YOU EDIT TEXT IN THIS PAGE, AND CREATE STUFF, YOU HAVE TO MIGRATE AND UPDATE


class Charachters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charachter_name = db.Column(db.String(120), unique=True, nullable=False)
    home_planet = db.Column(db.String(120), primary_key=True)
    persons_age = db.Column(db.Integer, primary_key=True)
    persons_species = db.Column(db.String(120), primary_key=True)

    def __repr__(self):
        return '<Charachters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.charachter_name,
            "home_planet": self.home_planet,
            "age": self.persons_age,
            "species": self.persons_species
            # do not serialize the password, its a security breach
        }

    class Favourites(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        likedPlanets = "something"
        likedCharachters = "something"

    def serialize(self):
        return "ok"
