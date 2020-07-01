from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Player, PlayerSeasonStats


class PlayerResource(resources.ModelResource):
    class Meta:
        model = Player


class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource


class PlayerSeasonStatsResource(resources.ModelResource):
    class Meta:
        model = PlayerSeasonStats


class PlayerSeasonStatsAdmin(ImportExportModelAdmin):
    resource_class = PlayerSeasonStatsResource


admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerSeasonStats, PlayerSeasonStatsAdmin)
