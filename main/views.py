from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import status
from django.http import Http404
from main.models import *
from main.serializer import *
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from random import *
from .models import User as Users
import random 
import datetime


class InfoView(APIView): 
    def get(self, request):
        info = Info.objects.last()
        ser = InfoSerializer(info)

        return Response(ser.data) 



class BlogView(APIView):
    def get(self, requeest):
        blog = Blog.objects.all().order_by('-id')[:4]
        ser = BlogSerializer(blog, many=True)

        return Response(ser.data)   


class GameView(APIView):
    def get(self, request):
        game = Game.objects.all().order_by('-id')
        ser = GameSerializer(game, many=True)

        return Response(ser.data)

class UserView(APIView):
    def post(self, request):
        try:
            a = request.POST.get('player_type')
            player_type = int(a)
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            game = int(request.POST.get('game'))
            phone = request.POST.get('phone')
            experience_from = request.POST.get('experience_from')
            experience_to = request.POST.get('experience_to')
            team_member = int(request.POST.get('team_member'))
            img = request.FILES['img']
            j = Game.objects.get(id=game)
            print(type(j.players), type(team_member), type(player_type))
            if j.is_started == False:
                if j.players == team_member and player_type == 2:
                    a = Users.objects.create(player_type=player_type, name=name, surname=surname, email=email,
                    game_id=game, phone=phone, experience_from=experience_from, experience_to=experience_to, team_member=team_member, 
                    img=img)
                    j.registrations += 1
                    j.save()
                    if j.registrations == j.team_quantity+1:
                        j.full = True
                        j.save()
                        return Response(status=404)
                    else:
                        ser = UserSerializer(a)
                        return Response(ser.data)

                elif j.players == team_member and player_type == 1 and int(team_member) == 1:
                    a = Users.objects.create(player_type=player_type, name=name, surname=surname, email=email,
                    game_id=game, phone=phone, experience_from=experience_from, experience_to=experience_to, team_member=team_member, 
                    img=img)
                    j.registrations += 1
                    j.save()
                    if j.registrations == j.team_quantity + 1:
                        j.full = True
                        j.save()
                        return Response(status=404)
                    else:
                        ser = UserSerializer(a)
                        return Response(ser.data)
                else:
                    return Response(status=404)
            else:
                return Response(status=404)
        except Exception as arr:
            data = {
                'error':f"{arr}"
            }
            return Response(data)


class PhotoView(APIView):
    def get(self, request):
        photo = Photo.objects.all().order_by('-id')[:10]
        ser = PhotoSerializer(photo, many=True)

        return Response(ser.data)


class NumberView(APIView):
    def get(self, request):
        number = Numbers.objects.all().order_by('-id')[:4]
        ser = NumbersSerializer(number, many=True)

        return Response(ser.data)


class EmailView(APIView):
    def post(self, request):
        email = EmailsSerializer(data=request.data)
        if email.is_valid():
            email.save()
            return Response(email.data, status=status.HTTP_201_CREATED)
        return Response(email.errors, status=status.HTTP_400_BAD_REQUEST)


class CompetitionView(APIView):
    def get(self, request):
        competition = Competition.objects.all().order_by('-id')[:4]
        ser = CompetitionSerializer(competition, many=True)

        return Response(ser.data)


# class Random_Competition(APIView):
#     def get(self,request,pk):
#         game = Game.objects.get(id=pk)
#         users = list(Users.objects.filter(game=game,is_active=True))
#         rn = int(len(users)/2)
#         for i in range(rn):
#             users_list = random.sample(users, k=2)
#             Competition.objects.create(game=game, user1=users_list[0], user2=users_list[1], data=str(datetime.datetime.now()))
#             for e in users_list:
#                 users.remove(e)
#         return Response({'status':True})





 
@login_required
def Admin_Home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    games = Game.objects.all()
    act = list(games)[0]
    if act.is_started == True:
        return redirect('start',act.id)
    context = {
        "games":games,
        "players":Users.objects.filter(game=list(games)[0],is_active=True),
        "active_game":act.id,
    }

    return render(request,"index.html",context)

@login_required
def Admin_Game(request,pk):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    games = Game.objects.all()
    act = Game.objects.get(id=pk)
    if act.is_started == True:
        return redirect('start',act.id)
    context = {
        "games":games,
        "players":Users.objects.filter(game__id=pk,is_active=True),
        "active_game":pk,
    }

    return render(request,"index.html",context)

def Admin_Start_Game(request,pk):
    game = Game.objects.get(id=pk)
    if request.method == 'POST':
        if game.is_started == True:
            for c in Competition.objects.filter(game=game):
                c.delete()
        users = list(Users.objects.filter(game=game,is_active=True))
        rn = int(len(users)/2)
        for i in range(rn):
            users_list = random.sample(users, k=2)
            Competition.objects.create(game=game, user1=users_list[0], user2=users_list[1], data=str(datetime.datetime.now()))
            for e in users_list:
                users.remove(e)
        
        game.is_started = True
        game.save()
        return redirect('start',pk)

def Admin_Start(request,pk):
    game = Game.objects.get(id=pk)

    competitions = Competition.objects.filter(game=game)
    context = {
        "competitions":competitions,
        "games":Game.objects.all(),
        "active_game":pk,
    }
    return render(request,"active.html",context)

def Admin_Dis_Active(request,pk):
    if request.method == "POST":
        id = request.POST["user"]
        user = Users.objects.get(id=int(id))
        user.is_active = False
        user.save()
    
    return redirect("start",pk)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username =request.POST.get("username")
        password = request.POST.get ('password')
        employe = User.objects.filter(username=username)
        if employe.count() > 0:
            if employe[0].check_password(password):
                login(request,employe[0])
                return redirect("home")
            else:
                return redirect('login')
        else:
            return redirect('login')    
    return render(request, 'login.html')