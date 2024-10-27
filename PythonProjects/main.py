import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cd6c51291019e6710916c54f4776c7bc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

# Переменные body, расставил в таком порядке для того чтобы можно было запустить все запросы подряд, а не вбивать данные самому.

body_create_pokemon = {
  "name": "generate",
  "photo_id": -1
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)
pokemon_id = response_create_pokemon.json()['id']




body_full_upd_pokemon = {
  "pokemon_id": pokemon_id,
  "name": "Ibra",
  "photo_id": 2
}

response_full_upd_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_full_upd_pokemon)
print(response_full_upd_pokemon.text)




body_add_pokeball = {
  "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post( url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
