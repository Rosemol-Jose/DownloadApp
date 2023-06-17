from rest_framework import serializers


#class AndroidAppSerializer(serializers.Modelserializer):
#from Website.android.models import Androidapp, User, AppDownload
from android.models import Androidapp,User, AppDownload


class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Androidapp
        fields = ['id', 'name', 'points']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'profile', 'points_earned', 'tasks_completed']


class AppDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDownload
        fields = ['id', 'app', 'user', 'screenshot']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

