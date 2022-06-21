from rest_framework import serializers
from main.models import *


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = '__all__'


class EmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = '__all__'
        
             
class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Competition
        fields = '__all__'
        
             
class ChampionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champions
        fields = '__all__'
