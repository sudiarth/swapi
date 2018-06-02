import requests, json
from pprint import pprint

API = 'http://35.153.66.157/api/{}/{}'

def get_request(url):
    response = requests.get(url)
    return json.loads(response.text)

class Club():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.terrain = data['city']
        self.climate = data['league']

    def print_info(self):
        print('Club ID: {}'.format(self.id))
        print('Club Name: {}'.format(self.name))
        print('Club Climate: {}'.format(self.city))
        print('Club Terrain: {}'.format(self.league))

class City():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.population = data['population']
        self.zipcode = data['zipcode']
        self.is_capital = data['is_capital']

    def __str__(self):
        return '{}\n{}\n{}\n{}'.format(self.id, self.name, self.population, self.zipcode, self.is_capital)

class Person():

    def parse_json(self, data):
        self.id = data['id']
        self.gender = data['gender']
        self.first = data['first']
        self.last = data['last']
        self.current_address = data['current_address']

        self.past_addresses = []
        for past_address in data['past_addresses']:
            self.past_addresses.append(past_address)

    def print_info(self):
        print('Name: {} {}'.format(self.first, self.last))
        print('Gender: {}'.format(self.gender))
        print('Past address: {}'.format(self.past_addresses))
        print('----------')

def print_people(number):
    for page_id in range(1, number):
        person = Person()
        person.parse_json(get_request(API.format('people', page_id)))
        person.print_info()

print_people(5)