import requests, json
from pprint import pprint

from base import DbManager
from models import Person, Planet, Species, Starship, Vehicle

DB = DbManager()

SWAPI_URL = 'https://swapi.co/api/{}/'

def get_request(url):
    response = requests.get(url)
    return json.loads(response.text)

def get_count(type):
    response = get_request(SWAPI_URL.format(type))
    count = response['count']
    return count

def get_persons():
    count = get_count('people')
    for person_id in range(1, count+1):
        url = SWAPI_URL.format('people')+'{}/'.format(person_id)
        person = None
        try:
            person = DB.open().query(Person).filter(Person.api_url == url).one()
        except:
            obj = get_request(url)
            if 'name' in obj:
                person = Person()
                person.parse_json(obj)
                DB.save(person)
        
        if person:
            print(person.name)
            print('+++++++++++++++++')

def get_starships():
    count = get_count('starships')
    for starship_id in range(1, count+1):
        url = SWAPI_URL.format('starships')+'{}/'.format(starship_id)
        starship = None
        try:
            starship = DB.open().query(Starship).filter(Starship.api_url == url).one()
        except:
            obj = get_request(url)
            if 'name' in obj:
                starship = Starship()
                starship.parse_json(obj)
                DB.save(starship)
        if starship:
            print(starship.name)
            print('+++++++++++++++++')

def get_planets():
    count = get_count('planets')
    for planet_id in range(1, count+1):
        url = SWAPI_URL.format('planets')+'{}/'.format(planet_id)
        planet = None
        try:
            planet = DB.open().query(Planet).filter(Planet.api_url == url).one()
        except:
            obj = get_request(url)
            if 'name' in obj:
                planet = Planet()
                planet.parse_json(obj)
                DB.save(planet)
        if planet:
            print(planet.name)
            print('+++++++++++++++++')

def get_vehicles():
    count = get_count('vehicles')
    for vehicle_id in range(1, count+1):
        url = SWAPI_URL.format('vehicles')+'{}/'.format(vehicle_id)
        vehicle = None
        try:
            vehicle = DB.open().query(Vehicle).filter(Vehicle.api_url == url).one()
        except:
            obj = get_request(url)
            if 'name' in obj:
                vehicle = Vehicle()
                vehicle.parse_json(obj)
                DB.save(vehicle)
        if vehicle:
            print(vehicle.name)
            print('+++++++++++++++++')

def get_species():
    count = get_count('species')
    for species_id in range(1, count+1):
        url = SWAPI_URL.format('species')+'{}/'.format(species_id)
        species = None
        try:
            species = DB.open().query(Species).filter(Species.api_url == url).one()
        except:
            obj = get_request(url)
            if 'name' in obj:
                species = Species()
                species.parse_json(obj)
                DB.save(species)
        if species:
            print(species.name)
            print('+++++++++++++++++')

get_persons()
get_starships()
get_planets()
get_vehicles()
get_species()