from django.urls import path, include
from .views import add_musics, cult_details, cult_home, music_home, list_musics, add_cult,add_music_cult

urlpatterns = [
    path('', music_home, name='music_home'),
    path('list_musics', list_musics ,name='list_musics'),
    path('add_music', add_musics , name="add_music"),
    path('cult/cult_home', cult_home, name="cult_home"),
    path('cult/details/<int:cult_id>', cult_details, name='cult_details'),
    path('cult/add', add_cult, name='add_cult'),
    path('cult/<int:cult_id>/add-praise', add_music_cult,name='add-praise')
]
