
## Open the JSON file of pokemon data
## create variable "data" that represents the enitre pokedex list
import json

with open('pokedex.json', encoding='utf-8') as pokedex_file:
    data = json.load(pokedex_file)

def print_pokemon_names_by_language(pokedex_data):
    lang = input("Choose language (en, fr, zh, ja): ").lower()
    for pokemon in pokedex_data:
        if lang == 'fr':
            print(pokemon['name']['french'])
        elif lang == 'zh':
            print(pokemon['name']['chinese'])
        elif lang == 'ja':
            print(pokemon['name']['japanese'])
        else:
            print(pokemon['name']['english'])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#Based on user input, show all moves that pokemon  could learn based on type. For example, if Charizard is fire/fyling, show all fire and flying moves.

""" sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def receipt(orders):
    receipt= {}
    for order in orders:
        if order["name"] in receipt:
            receipt[order["name"]]["quantity"] += 1
        else:
            receipt[order["name"]] ={
                "price": order["price"],
                "quantity": 1
            }
    for order, value in receipt.items():
        price = value["price"] * value["quantity"]
        print(order, value["quantity"], price)

print(receipt(sushi_orders)) """




""" """ """ 
wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}
for dept, docs in wards.items():
    print(dept, docs)
    for doc in docs:
        if doc not in staff:
            staff[doc] = []
            staff[doc].append(dept)
    print(staff['Bob']) """