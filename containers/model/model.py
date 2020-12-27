import joblib
import pandas as pd
import numpy as np
import sqlalchemy
import tqdm
import os
from features import Features


db_name = os.environ.get('DB_NAME')
db_hostname = os.environ.get('DB_HOSTNAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
engine = sqlalchemy.create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_hostname}/{db_name}')


def __init__(self):
    pass

Features.__init__ = __init__


class Model:
    def __init__(self, model_goals, model_assists, features):
        self.model_goals = model_goals
        self.model_assists = model_assists
        self.features = features

    @classmethod
    def load(cls, path='source'):
        model_goals = joblib.load(f'{path}/model_goals.pkl')
        model_assists = joblib.load(f'{path}/model_assists.pkl')
        features = joblib.load(f'{path}/features.pkl')
        return cls(model_goals, model_assists, features)
    
    def predict(self, player_id, postseason, num_games, league):
        df = self.build_features(player_id, postseason).tail(1)
        df = self.set_num_games(df, num_games)
        df = self.set_league(df, league)
        goals = self.model_goals.predict(df[self.features])[0]
        assists = self.model_assists.predict(df[self.features])[0]
        return {'goals': max(goals, 0), 'assists': max(assists, 0)}
    
    @staticmethod
    def set_num_games(df, num_games):
        df['games'] = num_games
        return df
    
    @staticmethod
    def set_league(df, league):
        rating = pd.read_sql(f"select league_rating from league_rating where league = '{league}'", engine).loc[0]['league_rating']
        df['league_rating'] = rating
        return df
        
    def build_features(self, player_id, postseason):
        f = Features()
        df = self.get_player_stats(player_id, postseason)
        new_season = self.add_new_season(df)
        f.merged = df.append(new_season)
        f.merged = f.merged[[x for x in f.merged if '_lag' not in x]]
        f.merged.drop([f'{x}_{y}' for x in f.aggregates for y in f.stats_columns], axis=1, inplace=True)
        f.merged['draft_entry'] = f.merged['draft_entry'].astype(float)
        f.get_age_at_season()
        f.get_stats_per_game()
        f.get_lags()
        f.get_aggregates()
        return f.merged
    
    def get_player_stats(self, player_id, postseason=0):
        df = pd.read_sql(f"select * from features where player_id = '{player_id}' and postseason_flag = {postseason}", engine)
        df = df.sort_values('season')
        return df
    
    def add_new_season(self, df):
        new_season = df.tail(1).copy()
        new_season['season'] = new_season['season'].map(lambda x: str(int(x.split('-')[0])+1)+'-'+str(int(x.split('-')[1])+1))
        new_season['year'] += pd.offsets.DateOffset(years=1)
        return df