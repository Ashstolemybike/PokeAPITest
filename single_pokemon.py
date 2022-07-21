from single_pokemon_model import SinglePokemonModel
import requests

class SinglePokemon:

    name_limit = {'limit': 100}

    def __init__(self, s_pokemon):
        self.url = "https://pokeapi.co/api/v2/pokemon/" + s_pokemon
        self.request = requests.get(self.url)
        self.resp_json = self.request.json()

    def response_data(self):
        return SinglePokemonModel(self.resp_json)


