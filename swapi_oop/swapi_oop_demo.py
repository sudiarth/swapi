import requests, json
from pprint import pprint

SWAPI = 'https://swapi.co/api/{}/{}'

def get_request(url):
    response = requests.get(url)
    return json.loads(response.text)

class Planet():
    def __init__(self, data):
        self.name = data['name']
        self.terrain = data['terrain']
        self.climate = data['climate']

    def print_info(self):
        print('Homeworld Name: {}'.format(self.name))
        print('Homeworld Climate: {}'.format(self.climate))
        print('Homeworld Terrain: {}'.format(self.terrain))

class Starship():
    def __init__(self, data):
        self.name = data['name']
        self.manufacturer = data['manufacturer']
        self.model = data['model']

    def __str__(self):
        return '{}\n{}\n{}'.format(self.name, self.manufacturer, self.model)

class Person():

    def parse_json(self, data):
        self.name = data['name']
        self.birth_year = data['birth_year']
        self.gender = data['gender']

        homeworld_obj = get_request(data['homeworld'])
        self.homeworld = Planet(homeworld_obj)

        self.starships = []
        for starship_url in data['starships']:
            starship = Starship(get_request(starship_url))
            self.starships.append(starship)

    def print_info(self):
        print('Name: {}'.format(self.name))
        print('Birth Year: {}'.format(self.birth_year))
        print('Gender: {}'.format(self.gender))
        print('----------')
        self.homeworld.print_info()
        for starship in self.starships:
            print(starship)
        print('================')


def print_people(number):
    for person_id in range(1, number):
        person = Person()
        person.parse_json(get_request(SWAPI.format('people', person_id)))
        person.print_info()

print_people(5)