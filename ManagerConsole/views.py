from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Player


def players_view(request):
    ctx = {}
    template = 'index.html'
    div_parameter = request.GET.get("div")

    if request.is_ajax():
        if div_parameter == 'user-input':
            players = Player.objects.filter(name__icontains=request.GET.get("player_name"))
            html = render_to_string(
                template_name="players_list.html",
                context={"players": players}
            )
            return JsonResponse(data={"html_from_view": html}, safe=False)

        elif div_parameter == 'player-pick':
            player = Player.objects.filter(pk=request.GET.get("player_id")).first()
            html = render_to_string(
                template_name='player_card.html',
                context={"player": player}
            )
            return JsonResponse(data={"html_from_view": html}, safe=False)

    players = Player.objects.all()
    ctx["players"] = players
    return render(request, template, context=ctx)


# class PlayerDetailView(generic.DetailView):
#     template_name = 'player_card.html'
#     model = Player
