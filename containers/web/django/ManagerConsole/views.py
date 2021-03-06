import pandas as pd

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Player, PlayerSeasonStats
from .plotly import create_stats_graph


leagues = ["NHL", "VHL", "KHL"]


def players_view(request):
    ctx = {}
    template = 'index.html'
    div_parameter = request.GET.get("div")

    if request.is_ajax():
        if div_parameter == 'user-input':
            response = user_input_handler(request)
            return response

        elif div_parameter == 'player-pick':
            response = player_pick_handler(request)
            return response

        elif div_parameter == 'graph':
            predict = bool(request.GET.get('predict'))
            predict_params = dict(num_games=request.GET.get('num_games'),
                                  player_id=request.GET.get('player_id'),
                                  postseason_flag=request.GET.get('playoff_switcher'),
                                  league=request.GET.get('league'))
            response = graph_filter_handler(request, predict=predict, predict_params=predict_params)
            return response

    players = Player.objects.order_by('name')[:11]
    ctx["players"] = players
    return render(request, template, context=ctx)


def user_input_handler(request):
    players = Player.objects.order_by('name').filter(name__icontains=request.GET.get("player_name"))[:11]
    html = render_to_string(
        template_name="players_list.html",
        context={"players": players}
    )
    return JsonResponse(data={"html_from_view": html}, safe=False)


def player_pick_handler(request):
    player, graph = get_graph(request)
    html = render_to_string(
        template_name='player_card.html',
        context={"player": player, 'graph': graph, 'leagues': leagues}
    )
    return JsonResponse(data={"html_from_view": html}, safe=False)


def graph_filter_handler(request, predict, predict_params=None):
    player, graph = get_graph(request, predict, predict_params)
    html = render_to_string(
        template_name='graph.html',
        context={'graph': graph}
    )
    return JsonResponse(data={"html_from_view": html}, safe=False)


def get_graph(request, predict=False, predict_params=None):
    playoff_switcher = 1 if request.GET.get("playoff_switcher") == 'playoff' else 0
    player = Player.objects.filter(pk=request.GET.get("player_id")).first()
    player_stats_queryset = PlayerSeasonStats.objects.filter(player=player.pk,
                                                             postseason_flag=playoff_switcher)
    player_stats = pd.DataFrame.from_records(player_stats_queryset.values())
    graph = create_stats_graph(player_stats, predict, predict_params)
    return player, graph

