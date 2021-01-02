import plotly.graph_objs as go
import pandas as pd
from .predict import predict


assist_color = 'rgba(173, 216, 230, 0.6)'
goal_color = 'rgba(243, 38, 130, 0.6)'
marker_line_color = 'rgba(228, 228, 218, 0.8)'
prediction_line_color = 'lightgreen'


def create_stats_graph(player_stats_df, predict=False, predict_params=None):
    try:
        stats = player_stats_df.groupby(['season'])['goals', 'assists',
                                                    'games'].sum().reset_index().sort_values('season')
    except KeyError:
        stats = pd.DataFrame([{'season': '', 'goals': '', 'assists': '', 'games': ''}])

    goals_colors = [goal_color] * stats.shape[0]
    assists_colors = [assist_color] * stats.shape[0]
    marker_line_colors = [marker_line_color] * stats.shape[0]
    if predict:
        stats = make_prediction(stats, predict_params)
        goals_colors.append(goal_color)
        assists_colors.append(assist_color)
        marker_line_colors.append(prediction_line_color)

    year = [str(x)[2:] for x in stats.season.tolist()]

    # Внешний вид
    fig = go.Figure(
        layout=go.Layout(
            legend=dict(
                font=dict(
                    family="Verdana",
                    size=22,
                    color="white"
                )),
            xaxis=dict(type='category'),
            paper_bgcolor='rgba(0,0,0,0.0)',
            plot_bgcolor='rgba(0,0,0,0.0)',
            modebar=dict(bgcolor='rgba(0,0,0,0.0)', color='white', activecolor='rgba(243, 38, 130, 0.3)'),
            title=go.layout.Title(text="Season stats",
                                  font=dict(family='Verdana', size=22, color='white'))
        )
    )

    # Оси
    fig.update_xaxes(tickfont=dict(family='Verdana', size=18, color='white'))
    fig.update_yaxes(tickfont=dict(family='Verdana', size=18, color='white'))

    # Данные
    fig.add_trace(go.Bar(x=year, y=stats.goals.tolist(), name='Goals',
                         marker_color=goals_colors, marker_line_width=3, marker_line_color=marker_line_colors))
    fig.add_trace(go.Bar(x=year, y=stats.assists.tolist(), name='Assists',
                         marker_color=assists_colors, marker_line_width=3, marker_line_color=marker_line_colors))
    fig.add_trace(go.Scatter(x=year, y=stats.games.tolist(), name='Games', line=dict(color='royalblue', width=3)))
    # Стакаем голы и ассисты
    fig.update_layout(barmode='stack', autosize=True)

    graph = fig.to_html(full_html=True, include_plotlyjs=False)
    return graph


def make_prediction(stats, predict_params):
    postseason_flag = 1 if predict_params['postseason_flag'] == 'playoff' else 0
    prediction = predict(predict_params['player_id'], postseason_flag,
                         predict_params['num_games'], predict_params['league'])
    games = predict_params['num_games']
    goals = int(prediction['goals'])
    assists = int(prediction['assists'])
    season = prediction['season']
    stats = stats.append(pd.DataFrame([{'goals': goals, 'assists': assists,
                                        'season': season, 'games': games}]))
    return stats
