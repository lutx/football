from django.contrib import admin

# Register your models here.
from competition.models import *
admin.site.register(LeagueType)
admin.site.register(Match)
admin.site.register(Kolejka)
admin.site.register(Team)
admin.site.register(Table)
admin.site.register(Player)
admin.site.register(MatchFacts)