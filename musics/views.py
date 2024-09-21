from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.messages import constants
from django.contrib import messages
from django.conf import settings
import json
import requests

from adjaf_mf3_3etp.utils import Requests
# Create your views here.

def music_home(request):
    return render(request,'musics/home_music.html')

def list_musics(request):
    req = Requests(settings.MUSIC_API_HOST)
    response = req.get("music/get-musics")
    musics = []
    if response:
        musics = response["data"]
    else:
        messages.add_message(request, constants.ERROR, "Error interno por favor entrar em contato com o ADM do sistema !")
        
    return render(request, 'musics/list_musics.html', context={"musics": musics})

def add_musics(request):
    
    method = request.method
    if method == "POST":
        name = request.POST.get("name")
        letter = request.POST.get("letter") 
        singer = request.POST.get("singer")
        music = request.FILES.get("music")
       
        music_json = {
            "name": name,
            "letter": letter,
            "singer": singer
        }
        files = {
            'file': (music.name, music, music.content_type),
            'music_json': (None, json.dumps(music_json), 'application/json')
        }
        response = requests.post(F"{settings.MUSIC_API_HOST}/music/create-music", files=files)
        messages.add_message(request, constants.SUCCESS, "Musica adicionada com sucesso") if response.ok else messages.add_message(request, constants.ERROR, "Não foi possivel adicionar a musica. tente novamente mais tarde")
        return redirect("/musics/list_musics")

        
    return render(request, "musics/add_music.html")

def cult_home(request):
    req = Requests(settings.MUSIC_API_HOST)
    response = req.get("cult/get-cults")
    cults = []
    if response: 
        cults = response["data"]
    else:
        messages.add_message(request, constants.ERROR, "Error interno por favor entrar em contato com o ADM do sistema !")
    return render(request, "cult/home_cult.html",context={"cults": cults})


def cult_details(request, cult_id: int):
    req = Requests(settings.MUSIC_API_HOST)
    response = req.get(f"cult/get-cult/{cult_id}")
    cult = {}
    if response:
        
        cult = response["data"]
    else:
        messages.add_message(request, constants.ERROR, "Não foi possivel carregar o culto ")
    print(cult)
    return render(request, "cult/cult_details.html", context={"cult": cult})

def add_cult(request):
    method = request.method
    if method == "POST":
        req = Requests(settings.MUSIC_API_HOST)
        name = request.POST.get("name")
        data = request.POST.get("date") 

        music = {
        "name": name,
        "endDate": data
        }
        response = req.post("cult/create-cult",body=music)
        if response:   
            messages.add_message(request, constants.SUCCESS, "Culto Criado com sucesso")
        return redirect("/musics/cult/cult_home")
    return render(request, "cult/add_cult.html")

def add_music_cult(request, cult_id: int):
    method = request.method
    if method == "POST":
        group = request.POST.get("group")
        music = request.POST.get("music")
        body = {
            "cultId": cult_id,
            "musicId": music,
            "groupId": group
        }
        req = Requests(settings.MUSIC_API_HOST)
        response = req.post("cult/add-praise",body=body)
        
        if not response:
            messages.add_message(request, constants.SUCCESS, "Culto Criado com sucesso")
        return redirect(f"/musics/cult/details/{cult_id}")
    
    req = Requests(settings.MUSIC_API_HOST)
    musics = []
    groups = []
    response_music = req.get("music/get-musics")
    response_groups = req.get("group/get_groups")
    if response_music:
        musics = response_music
    if response_groups:
        groups = response_groups
    
    return render(request, "cult/add_music_cult.html", context={"musics": musics["data"], "groups": groups["data"],"cult_id": cult_id})
