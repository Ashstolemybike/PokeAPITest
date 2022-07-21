class SinglePokemonModel:

    def __init__(self, single_pokemon):
        self.abilities = single_pokemon['abilities']
        self.ability1 = self.abilities[0]
        self.ability2 = self.abilities[1]
        self.base_experience = single_pokemon['base_experience']
        self.forms = single_pokemon['forms']
        self.formname = self.forms[0]['name']
        self.formurl = self.forms[0]['url']
        self.game_indices = single_pokemon['game_indices']
        #self.game_1_index = self.game_indices[0]['game_index']
        self.game_1_version = self.game_indices[0]['version']
        self.game_1_details = self.game_1_version['name'], self.game_1_version['url']
        self.game_2_version = self.game_indices[1]['version']
        self.game_2_details = self.game_2_version['name'], self.game_1_version['url']
        self.game_3_version = self.game_indices[2]['version']
        self.game_3_details = self.game_3_version['name'], self.game_1_version['url']
        self.game_4_version = self.game_indices[3]['version']
        self.game_4_details = self.game_4_version['name'], self.game_1_version['url']
        self.game_5_version = self.game_indices[4]['version']
        self.game_5_details = self.game_5_version['name'], self.game_1_version['url']
        self.game_6_version = self.game_indices[5]['version']
        self.game_6_details = self.game_6_version['name'], self.game_1_version['url']
        self.game_7_version = self.game_indices[6]['version']
        self.game_7_details = self.game_7_version['name'], self.game_1_version['url']
        self.game_8_version = self.game_indices[7]['version']
        self.game_8_details = self.game_8_version['name'], self.game_1_version['url']
        self.game_9_version = self.game_indices[8]['version']
        self.game_9_details = self.game_9_version['name'], self.game_1_version['url']
        self.game_10_version = self.game_indices[9]['version']
        self.game_10_details = self.game_10_version['name'], self.game_1_version['url']
        self.game_11_version = self.game_indices[10]['version']
        self.game_11_details = self.game_11_version['name'], self.game_1_version['url']
        self.game_12_version = self.game_indices[11]['version']
        self.game_12_details = self.game_12_version['name'], self.game_1_version['url']
        self.game_13_version = self.game_indices[12]['version']
        self.game_13_details = self.game_13_version['name'], self.game_1_version['url']
        self.game_14_version = self.game_indices[13]['version']
        self.game_14_details = self.game_14_version['name'], self.game_1_version['url']
        self.game_15_version = self.game_indices[14]['version']
        self.game_15_details = self.game_15_version['name'], self.game_1_version['url']
        self.game_16_version = self.game_indices[15]['version']
        self.game_16_details = self.game_16_version['name'], self.game_1_version['url']
        self.game_17_version = self.game_indices[16]['version']
        self.game_17_details = self.game_17_version['name'], self.game_1_version['url']
        self.game_18_version = self.game_indices[17]['version']
        self.game_18_details = self.game_18_version['name'], self.game_1_version['url']
        self.game_19_version = self.game_indices[18]['version']
        self.game_19_details = self.game_19_version['name'], self.game_1_version['url']
        self.game_20_version = self.game_indices[19]['version']
        self.game_20_details = self.game_20_version['name'], self.game_1_version['url']



