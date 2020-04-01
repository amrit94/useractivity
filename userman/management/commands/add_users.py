from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from userman.models import Profile, TIMEZONES
import csv

TIMEZONES = dict(TIMEZONES)


class Command(BaseCommand):
    help = 'Using Json file'

    def handle(self, *args, **options):
        with open("bin/users.csv", 'r') as file:
            users_reader = csv.DictReader(file)
            for user in users_reader:
                user_dict = dict(user)
                user_obj, created = User.objects.update_or_create(
                    username=user_dict['firstname'] + user_dict['lastname'],
                    is_active=True,
                    password="password",
                    first_name=user_dict['firstname'],
                    last_name=user_dict['lastname'],
                )
                Profile.objects.update_or_create(user=user_obj,
                                                 userid=user_dict['id'],
                                                 timezone=TIMEZONES[user_dict['timezone']])
