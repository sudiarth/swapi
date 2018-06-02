import requests, json
from pprint import pprint

from base import DbManager
from models import Person, Club, Department, League, Company, State, Exchange, City

DB = DbManager()

CK_API_URL_PAGE = 'http://35.153.66.157/api/{}/{}'
CK_API_URL = 'http://35.153.66.157/api/{}/'

def get_request(url):
    response = requests.get(url)
    return json.loads(response.text)

def get_person():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL_PAGE.format('people', page_id)
            response = get_request(url)
            for person_data in response:
                try:
                    return DB.open().query(Person).filter(Person.api_url == person_data['api']).one()
                except:
                    obj = get_request(person_data['api'])
                    if 'id' in obj:
                        person = Person()
                        person.parse_json(obj)
                        DB.save(person)
                    
                    if person:
                        print('SAVED PERSON ID {}'.format(person.id))
                        print('+++++++++++++++++')
        except:
            pass
            

def get_club():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL_PAGE.format('clubs', page_id)
            response = get_request(url)
            for club_data in response:
                try:
                    return DB.open().query(Club).filter(Club.api_url == club_data['api']).one()
                except:
                    obj = get_request(club_data['api'])
                    if 'id' in obj:
                        club = Club()
                        club.parse_json(obj)
                        DB.save(club)
                    
                    if club:
                        print('SAVED CLUB ID {}'.format(club.id))
                        print('+++++++++++++++++')
        except:
            pass

def get_department():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL_PAGE.format('departments', page_id)
            response = get_request(url)
            for department_data in response:
                try:
                    return DB.open().query(Department).filter(Department.api_url == department_data['api']).one()
                except:
                    obj = get_request(department_data['api'])
                    if 'id' in obj:
                        department = Department()
                        department.parse_json(obj)
                        DB.save(department)
                    
                    if department:
                        print('SAVED DEPARTMENT ID {}'.format(department.id))
                        print('+++++++++++++++++')
        except:
            pass

def get_league():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL.format('leagues')
            response = get_request(url)
            for league_data in response:
                try:
                    return DB.open().query(League).filter(League.api_url == league_data['api']).one()
                except:
                    obj = get_request(league_data['api'])
                    if 'id' in obj:
                        league = League()
                        league.parse_json(obj)
                        DB.save(league)
                    
                    if league:
                        print('SAVED LEAGUE ID {}'.format(league.id))
                        print('+++++++++++++++++')
        except:
            pass

def get_company():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL_PAGE.format('companies', page_id)
            response = get_request(url)
            for company_data in response:
                try:
                    return DB.open().query(Company).filter(Company.api_url == company_data['api']).one()
                except:
                    obj = get_request(company_data['api'])
                    if 'id' in obj:
                        company = Company()
                        company.parse_json(obj)
                        DB.save(company)
                    
                    if company:
                        print('SAVED COMPANY ID {}'.format(company.id))
                        print('+++++++++++++++++')
        except:
            pass

def get_state():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL.format('states')
            response = get_request(url)
            for state_data in response:
                try:
                    return DB.open().query(State).filter(State.api_url == state_data['api']).one()
                except:
                    obj = get_request(state_data['api'])
                    if 'id' in obj:
                        state = State()
                        state.parse_json(obj)
                        DB.save(state)
                    
                    if state:
                        print('SAVED STATE ID {}'.format(state.id))
                        print('+++++++++++++++++')
        except:
            pass

def get_exchange():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL.format('exchanges')
            response = get_request(url)
            for exchange_data in response:
                try:
                    return DB.open().query(Exchange).filter(Exchange.api_url == exchange_data['api']).one()
                except:
                    obj = get_request(exchange_data['api'])
                    if 'id' in obj:
                        exchange = Exchange()
                        exchange.parse_json(obj)
                        DB.save(exchange)
                    
                    if exchange:
                        print('SAVED EXCHANGE ID {}'.format(exchange.id))
                        print('+++++++++++++++++')
        except:
            pass

def get_city():
    for page_id in range(1, 2):
        try:
            url = CK_API_URL_PAGE.format('cities', page_id)
            response = get_request(url)
            for city_data in response:
                try:
                    return DB.open().query(City).filter(City.api_url == city_data['api']).one()
                except:
                    obj = get_request(city_data['api'])
                    if 'id' in obj:
                        city = City()
                        city.parse_json(obj)
                        DB.save(city)
                    
                    if city:
                        print('SAVED CITY ID {}'.format(city.id))
                        print('+++++++++++++++++')
        except:
            pass

get_person()
get_club()
get_department()
get_league()
get_company()
get_state()
get_exchange()
get_city()