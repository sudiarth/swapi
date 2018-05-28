import json
import requests
from pprint import pprint

api_url = 'https://swapi.co/api/people/'

def get_request(url):
    try:
        response = requests.get(url)
        obj = json.loads(response.text)
        return obj
    except:
        return

def get_homeworld(url):
    try:
        response = requests.get(url)
        obj = json.loads(response.text)
        return obj
    except:
        return 'n/a'

def get_starships(url):
    try:
        if(len(url) > 1):
            arr = []
            for i in range(0, len(url)):
                response = requests.get(url[i])
                obj = json.loads(response.text)
                arr.append(obj)
            return arr
        else:
            response = requests.get(url)
            obj = json.loads(response.text)
            return obj
    except:
        return 'n/a'

def get_vehicles(url):
    try:
        if(len(url) > 1):
            arr = []
            for i in range(0, len(url)):
                response = requests.get(url[i])
                obj = json.loads(response.text)
                arr.append(obj)
            return arr
        else:
            response = requests.get(url)
            obj = json.loads(response.text)
            return obj
    except:
        return 'n/a'

def get_all_peoples():
    count = get_request('{}'.format(api_url))
    for i in range(1, count["count"]+1):
        try:

            response = get_request('{}{}'.format(api_url,i))
            homeworld = get_homeworld(response["homeworld"])
            starships = get_starships(response["starships"])
            vehicles = get_vehicles(response["vehicles"])

            print('No. {}'.format(i))
            print('Name: {}'.format(response["name"]))
            print('Birth year: {}'.format(response["birth_year"]))
            print('Gender: {}'.format(response["gender"]))

            home_name = homeworld["name"]
            home_climate = homeworld["climate"]
            home_terain = homeworld["terrain"]

            print('Homeworld: - {}'.format(home_name))
            print('             {}'.format(home_climate))
            print('             {}'.format(home_terain))
        
            
            if(starships != 'n/a'):
                for starship in starships:
                    starship_name = starship["name"]
                    starship_model = starship["model"]
                    starship_manufacturer = starship["manufacturer"]

                    print('Starships: - {}'.format(starship_name))
                    print('             {}'.format(starship_model))
                    print('             {}'.format(starship_manufacturer))
            else:
                print('n/a')

            if(vehicles != 'n/a'):
                for vehicle in vehicles:
                    vehicle_name = vehicle["name"]
                    vehicle_model = vehicle["model"]
                    vehicle_manufacturer = vehicle["manufacturer"]

                    print('Vehicles:  - {}'.format(vehicle_name))
                    print('             {}'.format(vehicle_model))
                    print('             {}'.format(vehicle_manufacturer))
            else:
                print('n/a')

            print('')
        except:
            print('error')

get_all_peoples()