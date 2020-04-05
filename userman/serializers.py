from rest_framework import serializers
from userman.models import Profile, ActivityPeriod
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

    def get_start_time(self, obj):
        return obj.start_time


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('get_userid')  # change field name
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'real_name', 'timezone', 'activity_periods')

    def get_userid(self, obj):
        return obj.userid
