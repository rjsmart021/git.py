import json
from unicodedata import name
import requests
from pprint import PrettyPrinter
import requests
import requests
import pprint as pp 
   
# Making a GET request 
r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu') 
# check status code for response received 
print(r) 
#print content of request 
print(r.content) 
name_or_id = "stench"  
url = "https://pokeapi.co/api/v2/pokemon/pikachu/{}/".format(name_or_id)
response = requests.get(url)
if response.status_code != 200: 
    print(response.text)
else:
    data = response.json()
    #pp.pprint(data)

    print('\n--- data.keys() ---\n')
    print(data.keys())
    
    print('\n--- data["name"] ---\n')
    print(data['name'])

    print('\n--- data["names"] ---\n')
    pp.pprint(data["names"])
    
    print('\n--- data["names"][0]["name"] ---\n')
    print(data['names'][0]['name'])
    
    print('\n--- abilities : name ---\n')
    names = []
for item in data["names"]:
    print(item['abilities']['name'],":", item["name"])
    names.append( item["name"] )
        
    print('\n--- after for-loop ---\n')
    print(names)
url = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

for offset in range(0, 1000, 100):
    params['offset'] = offset  # add new value to dict with `limit`
    response = requests.get(url, params=params)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        #pp.pprint(data)
        for item in data['results']:
            print(item['name'])
#2. Extract and print the name and abilities of the Pokémon.
#Expected Outcome: The script should output the name of the 
#Pokémon (Pikachu) and a list of its abilities.

print(response.json().keys())
#storing all the record in a variable called results
results = response.json()['names']
#storing all the record in a variable called results
results = response.json()['abilities']
#Task 3: Analyzing and Displaying Data
#1. Modify the script to fetch data for three different Pokémon.

#2. Create a function to calculate and return the average weight of these Pokémon.
def fetch_pokemon_data(pokemon_name):
    response = requests.get(url)
    pokemon = response.json()['names']
    response.json()['abilities']
    r= requests.get(url)
    status = r.status_code 
    if status != 200: 
        quit()
    else: 
        get_pokedex(status)
        
def calculate_average_weight(pokemon_list):
    #Pokemon list is a list of Pokemon Weights
    pokemon_list = []
        return average(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
for planet in planets:
    if planet['isPlanet']:
        name = #get planet English name
        mass = #get planet mass
        orbit_period = #get planet orbit period
        print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

#Task 3: Data Presentation and Analysis - Perform a simple analysis, 
#such as finding the planet with the longest orbit period or the heaviest planet. 
length(orbit_period)
import requests
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = self.name
            mass = self.mass
            orbit_period = #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planet[]

def find_heaviest_planet(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = self.name
            mass = self.mass
    return max(mass) 

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
find_heaviest_planet(planets)
