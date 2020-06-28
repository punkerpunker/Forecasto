from django.urls import include, path

from . import views

app_name = 'HockeyManager'
urlpatterns = [
    path('', views.players_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('player/<int:pk>', views.PlayerDetailView.as_view(), name='player')
]
