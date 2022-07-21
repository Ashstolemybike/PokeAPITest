class SinglePokemonModel:

    def __init__(self, single_pokemon):
        self.abilities = single_pokemon['abilities']
        self.ability1 = self.abilities[0]
