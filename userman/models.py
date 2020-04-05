from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.CharField(max_length=10, unique=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES,
                                default='UTC')

    def __str__(self):
        return self.user.username

    @property
    def real_name(self):
        return self.user.first_name + ' ' + self.user.last_name


class ActivityPeriod(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
