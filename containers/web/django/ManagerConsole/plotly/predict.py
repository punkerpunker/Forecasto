import requests
import os

model_host = os.environ.get('MODEL_HOST')
endpoint = 'http://model:1769/predict'


def predict(player_id, postseason_flag, num_games, league):
    resp = requests.get(endpoint, params={'player_id': player_id,
                                          'postseason_flag': postseason_flag,
                                          'num_games': num_games,
                                          'league': league})
    return resp.json()
