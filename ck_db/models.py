from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from base import Base, inverse_relationship, create_tables

# ADD MODELS

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)

    first = Column(String)
    last = Column(String)
    gender = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.first = obj['first']
        self.last = obj['last']
        self.gender = obj['gender']

class Club(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    company = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']
        self.company = obj['company']

class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    sport = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']
        self.sport = obj['sport']

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    total_assets = Column(Integer)
    revenue = Column(Integer)
    net_income = Column(Integer)
    operating_income = Column(Integer)
    founded_on = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']
        self.total_assets = obj['total_assets']
        self.revenue = obj['revenue']
        self.net_income = obj['net_income']
        self.operating_income = obj['operating_income']
        self.founded_on = obj['founded_on']

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    gdp = Column(Integer)
    abbreviation = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']
        self.gdp = obj['gdp']
        self.abbreviation = obj['abbreviation']

class Exchange(Base):
    __tablename__ = 'exchanges'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    city = Column(Integer)
    address = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']
        self.city = obj['city']
        self.address = obj['address']

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)

    api_id = Column(Integer, unique=True)
    api_url = Column(String, unique=True)
    name = Column(String, unique=True)

    population = Column(Integer)
    zipcode = Column(String)
    is_capital = Column(Integer)
    state = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_json(self, obj):
        self.api_id = obj['id']
        self.api_url = obj['api']
        self.name = obj['name']
        self.population = obj['population']
        self.zipcode = obj['zipcode']
        self.is_capital = obj['is_capital']
        self.state = obj['state']

# ADD MODELS 


if __name__ is not '__main__':
    create_tables()