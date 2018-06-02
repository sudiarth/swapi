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
        obj = get_request(url)
        return obj
    except:
        return 'Not Found'

def get_all_peoples():
    dictionary = get_request('{}'.format(api_url))
    for i in range(1, dictionary["count"]+1):
        try:
            response    = get_request('{}{}'.format(api_url,i))
            homeworld   = get_homeworld(response["homeworld"])
            starships   = get_starships(response["starships"])
            vehicles    = get_vehicles(response["vehicles"])

            d_peoples   = {}

            if(homeworld != 'n/a'):
                d_peoples["planet"] = homeworld["name"]
                d_peoples["climate"] = homeworld["climate"]
                d_peoples["terrain"] = homeworld["terrain"]
            else:
                d_peoples["planet"] = 'n/a'
                d_peoples["climate"] = 'n/a'
                d_peoples["terrain"] = homeworld["terrain"]

            d_peoples["name"] = response["name"]
            d_peoples["gender"] = response["gender"]

            print(d_peoples)

            return d_peoples

        except:
            return

def get_starships(url):
    try:
        if(len(url) > 1):
            arr = []
            for i in range(0, len(url)):
                obj = get_request(url[i])
                arr.append(obj)
            return arr
        else:
            obj = get_request(url)
            return obj
    except:
        return 'n/a'

def get_vehicles(url):
    try:
        if(len(url) > 1):
            arr = []
            for i in range(0, len(url)):
                obj = get_request(url[i])
                arr.append(obj)
            return arr
        else:
            obj = get_request(url)
            return obj
    except:
        return 'n/a'

def print_vehicles(arr):
    for i in range(0, len(arr)):
        try:
            for vehicle in arr:
                name = vehicle["name"]
                model = vehicle["model"]
                manufacturer = vehicle["manufacturer"]

                print('Vehicles:  - {}'.format(name))
                print('             {}'.format(model))
                print('             {}'.format(manufacturer))
            return
        except:
            return

def print_starships(arr):
    for i in range(0, len(arr)):
        try:
            for starship in arr:
                name = starship["name"]
                model = starship["model"]
                manufacturer = starship["manufacturer"]

                print('Starships: - {}'.format(name))
                print('             {}'.format(model))
                print('             {}'.format(manufacturer))
            return
        except:
            return

def print_all_peoples():
    dictionary = get_request('{}'.format(api_url))
    for i in range(1, dictionary["count"]+1):
        try:

            response    = get_request('{}{}'.format(api_url,i))
            homeworld   = get_homeworld(response["homeworld"])
            starships   = get_starships(response["starships"])
            vehicles    = get_vehicles(response["vehicles"])

            print('No. {}'.format(i))
            print('Name: {}'.format(response["name"]))
            print('Birth year: {}'.format(response["birth_year"]))
            print('Gender: {}'.format(response["gender"]))

            if(homeworld != 'n/a'):
                home_name = homeworld["name"]
                home_climate = homeworld["climate"]
                home_terain = homeworld["terrain"]
                print('Homeworld: - {}'.format(home_name))
                print('             {}'.format(home_climate))
                print('             {}'.format(home_terain))
            else:
                print('n/a')
        
            
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
            print('')
            print('n/a')
            print('')

def print_vehicles_starships(number):
    for i in range(1, number+1):
        response    = get_request('{}{}'.format(api_url,i))
        try:
            print('No. {}'.format(i))
            print('Name: {}'.format(response["name"]))
            print('Birth year: {}'.format(response["birth_year"]))
            print('Gender: {}'.format(response["gender"]))

            print_vehicles(get_vehicles(response["vehicles"]))
            print_starships(get_starships(response["starships"]))

            print('')
        except:
            print('')
            print('n/a')
            print('')

def print_pilot(starship):
    try:
        response = print_all_peoples()
        for starship in starships:
            if(starship["name"] == starship):
                print('No. {}'.format(i))
                print('Name: {}'.format(response["name"]))
                print('Birth year: {}'.format(response["birth_year"]))
                print('Gender: {}'.format(response["gender"]))

        print('')
    except:
        print('')
        print('n/a')
        print('')

dictionary = get_request('{}'.format(api_url))

# Print all peoples
# print_peoples(dictionary["count"])

# Print out the names of the first 10 people
# print_peoples(10)

# Print out the vehicles and starships of the first 10 people
# print_vehicles_starships(10)

# Print out the names of people who fly X-wing fighters
# print_pilot('X-wing')
get_all_peoples()