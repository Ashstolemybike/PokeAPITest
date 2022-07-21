import json
import requests

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(pokemon)

resp = pokemon.json()
print(resp)