import connexion
import os
from model import Model


model = Model.load(path='source')


def predict(player_id, postseason_flag, num_games, league):
    return model.predict(player_id, postseason_flag, num_games, league), 200


app = connexion.App(__name__, specification_dir='.')
app.add_api('swagger.yaml')
app.run(port=os.environ.get('PORT'))
