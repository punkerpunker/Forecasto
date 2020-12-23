import pandas as pd

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Player, PlayerSeasonStats
from .plotly import create_stats_graph


def players_view(request):
    ctx = {}
    template = 'index.html'
    div_parameter = request.GET.get("div")

    if request.is_ajax():
        if div_parameter == 'user-input':
            players = Player.objects.order_by('name').filter(name__icontains=request.GET.get("player_name"))[:10]
            html = render_to_string(
                template_name="players_list.html",
                context={"players": players}
            )
            return JsonResponse(data={"html_from_view": html}, safe=False)

        elif div_parameter == 'player-pick':
            playoff_switcher = 1 if request.GET.get("playoff_switcher") == 'playoff' else 0
            print(playoff_switcher)
            player = Player.objects.filter(pk=request.GET.get("player_id")).first()
            player_stats_queryset = PlayerSeasonStats.objects.filter(player=player.pk,
                                                                     postseason_flag=playoff_switcher)
            player_stats = pd.DataFrame.from_records(player_stats_queryset.values())
            graph = create_stats_graph(player_stats)
            html = render_to_string(
                template_name='player_card.html',
                context={"player": player, 'graph': graph}
            )
            return JsonResponse(data={"html_from_view": html}, safe=False)

    players = Player.objects.order_by('name')[:10]
    ctx["players"] = players
    return render(request, template, context=ctx)
