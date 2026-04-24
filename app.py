
## Open the JSON file of pokemon data
## create variable "data" that represents the enitre pokedex list
import json
pokedex_file = open("./pokedex.json", encoding="utf-8")
data = json.load(pokedex_file)
pokedex_file.close()
search_term = input("Search for a Pokémon by name (e.g., 'Char'): ").lower()
matched_pokemon = []
for pokemon in data:
   if search_term in pokemon['name']['english'].lower():
       matched_pokemon.append(pokemon['name']['english'])
if len(matched_pokemon) == 0:
   print("No Pokémon found matching that name.\n")
else:
   print("Matches found:")
   for index, name in enumerate(matched_pokemon):
       print(str(index + 1) + ". " + name)
   print("\n") 
"""



"""
def languages(pokedex_data):
   lang = input("Choose language (english, french, chinese, japanese): ").lower()
   print("\n--- Pokémon List ---")
   for pokemon in pokedex_data:
       if lang == 'french':
           print(pokemon['name']['french'])
       elif lang == 'chinese':
           print(pokemon['name']['chinese'])
       elif lang == 'japanese':
           print(pokemon['name']['japanese'])
       else:
           print(pokemon['name']['english'])
   print("\n")
"""
"""
def pokemon_type(pokedex_data):
   search_type = input("Choose type (Grass, Fire, Water, Bug, Normal, etc.): ").capitalize()
  
   type_list = []
   for pokemon in pokedex_data:
       if search_type in pokemon['type']:
           type_list.append(pokemon)
  
   if len(type_list) == 0:
       print("No Pokémon found of type:", search_type)
   else:
       print("\n---", search_type, "type Pokémon ---")
       for pokemon in type_list:
           print(pokemon['name']['english'])
   return type_list  

def pokemoves():
   pokedex_file = open("./pokedex.json", encoding="utf-8")
   pokedex_data = json.load(pokedex_file)
   pokedex_file.close()
   moves_file = open("./moves.json", encoding="utf-8")
   moves_data = json.load(moves_file)
   moves_file.close()
   target_pokemon = input("Enter a Pokémon name to see compatible moves based on its type: ").lower()
   pokemon_types = []
   for pokemon in pokedex_data:
       if pokemon['name']['english'].lower() == target_pokemon:
           pokemon_types = pokemon['type']
   if len(pokemon_types) == 0:
       print("No Pokémon found named:", target_pokemon)
   else:
       print(target_pokemon.capitalize(), "is type:", pokemon_types)
       print("Moves it can learn:")
       found_moves = []
       for move in moves_data:
           if move['type'] in pokemon_types:
               found_moves.append(move['name'])
              
       if len(found_moves) == 0:
           print("No matching moves found in the database.")
       else:
           for index, move_name in enumerate(found_moves):
               print(str(index + 1) + " - " + move_name)

pokemoves()


        

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#Based on user input, show all moves that pokemon  could learn based on type. For example, if Charizard is fire/fyling, show all fire and flying moves.

"""  sushi_orders = [
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
] """

""" def receipt(orders):
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

print(receipt(sushi_orders))
 """
""" wards = {
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