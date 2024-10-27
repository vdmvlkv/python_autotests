import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cd6c51291019e6710916c54f4776c7bc'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '7551'



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_name_trainer():
    response_1 = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_1.json()["data"][0]["trainer_name"] == 'Оракул'

