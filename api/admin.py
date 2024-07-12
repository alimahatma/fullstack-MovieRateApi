from django.contrib import admin
from .models import Movie, Rating

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id','stars','movie_id','user_id')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)




