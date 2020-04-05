from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from userman.models import Profile, ActivityPeriod
from userman.serializers import ProfileSerializer, ActivityPeriodSerializer, UserSerializer
from django.contrib.auth.models import User


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ActivityPeriodList(generics.ListCreateAPIView):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
