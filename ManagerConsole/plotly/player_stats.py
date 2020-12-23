import plotly.graph_objs as go


def create_stats_graph(player_stats_df):
    stats = player_stats_df.groupby(['season'])['goals', 'assists', 'games'].sum().reset_index().sort_values('season')
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
    fig.add_trace(go.Bar(x=year, y=stats.goals.tolist(), name='Goals', marker_color='rgba(243, 38, 130, 0.5)'))
    fig.add_trace(go.Bar(x=year, y=stats.assists.tolist(), name='Assists',  marker_color='rgba(173, 216, 230, 0.8)'))
    fig.add_trace(go.Scatter(x=year, y=stats.games.tolist(), name='Games', line=dict(color='royalblue', width=3)))
    # Стакаем голы и ассисты
    fig.update_layout(barmode='stack')

    graph = fig.to_html(full_html=True)
    return graph
