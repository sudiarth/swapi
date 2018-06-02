from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from base import Base, inverse_relationship, create_tables

# ADD MODELS

class Person(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)

    api_url = Column(String, unique=True)

    name = Column(String, unique=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_url = obj['url']
        self.name = obj['name']
        self.height = obj['height']
        self.mass = obj['mass']
        self.hair_color = obj['hair_color']
        self.skin_color = obj['skin_color']
        self.eye_color = obj['eye_color']
        self.birth_year = obj['birth_year']
        self.gender = obj['gender']

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)

    api_url = Column(String, unique=True)
    name = Column(String, unique=True)
    mglt = Column(String)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(String)
    crew = Column(Integer)
    hyperdrive_rating = Column(Integer)
    length = Column(Integer)
    manufacturer = Column(String)
    max_atmosphering_speed = Column(String)
    model = Column(String)
    passengers = Column(Integer)
    starship_class = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    def parse_json(self, obj):
        self.api_url = obj['url']
        self.name = obj['name']
        self.mglt = obj['MGLT']
        self.cargo_capacity = obj['cargo_capacity']
        self.consumables = obj['consumables']
        self.cost_in_credits = obj['cost_in_credits']
        self.crew = obj['crew']
        self.hyperdrive_rating = obj['hyperdrive_rating']
        self.length = obj['length']
        self.manufacturer = obj['manufacturer']
        self.max_atmosphering_speed = obj['max_atmosphering_speed']
        self.model = obj['model']
        self.passengers = obj['passengers']
        self.starship_class = obj['starship_class']

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

    api_url = Column(String, unique=True)
    name = Column(String, unique=True)
    climate = Column(String)
    diameter = Column(Integer)
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    def parse_json(self, obj):
        self.api_url = obj['url']
        self.name = obj['name']
        self.climate = obj['climate']
        self.diameter = obj['diameter']
        self.gravity = obj['gravity']
        self.orbital_period = obj['orbital_period']
        self.population = obj['population']
        self.rotation_period = obj['rotation_period']
        self.surface_water = obj['surface_water']
        self.terrain = obj['terrain']

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)

    api_url = Column(String, unique=True)
    name = Column(String, unique=True)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    length = Column(Integer)
    manufacturer = Column(String)
    max_atmosphering_speed = Column(Integer)
    model = Column(String)
    passengers = Column(String)
    vehicle_class = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    def parse_json(self, obj):
        self.api_url = obj['url']
        self.name = obj['name']
        self.cargo_capacity = obj['cargo_capacity']
        self.consumables = obj['consumables']
        self.cost_in_credits = obj['cost_in_credits']
        self.crew = obj['crew']
        self.length = obj['length']
        self.manufacturer = obj['manufacturer']
        self.max_atmosphering_speed = obj['max_atmosphering_speed']
        self.model = obj['model']
        self.passengers = obj['passengers']
        self.vehicle_class = obj['vehicle_class']

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)

    api_url = Column(String, unique=True)
    name = Column(String, unique=True)
    average_height = Column(String)
    average_lifespan = Column(Integer)
    classification = Column(String)
    designation = Column(String)
    eye_colors = Column(String)
    hair_colors = Column(String)
    language = Column(String)
    skin_colors = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_url = obj['url']
        self.name = obj['name']
        self.average_height = obj['average_height']
        self.average_lifespan = obj['average_lifespan']
        self.classification = obj['classification']
        self.designation = obj['designation']
        self.eye_colors = obj['eye_colors']
        self.hair_colors = obj['hair_colors']
        self.language = obj['language']
        self.skin_colors = obj['skin_colors']

# ADD MODELS 


if __name__ is not '__main__':
    create_tables()