from django.contrib import admin
from .models import *


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 't_link', 'f_link', 'i_link', 'y_link')
admin.site.register(Info, InfoAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
admin.site.register(Blog, BlogAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','team_quantity', 'registrations', 'players','full', 'is_started')
admin.site.register(Game, GameAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_type', 'name', 'surname', 'email', 'game', 'phone', 'experience_from', 'experience_to', 'team_member', 'is_active')
admin.site.register(User, UserAdmin)


admin.site.register(Photo)


class NumbersAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'number')
admin.site.register(Numbers, NumbersAdmin)


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
admin.site.register(Emails, EmailsAdmin)


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id','game', 'user1', 'user2', 'data', 'active')
admin.site.register(Competition, CompetitionAdmin)


class ChampionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'one', 'two', 'three', 'date')
admin.site.register(Champions, ChampionsAdmin)