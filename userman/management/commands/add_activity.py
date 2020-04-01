from django.core.management.base import BaseCommand
from userman.models import Profile, ActivityPeriod
import csv, pytz
from datetime import datetime, timedelta
from email.utils import parsedate_tz, mktime_tz


def conv_time(some_time):
    timestamp = mktime_tz(parsedate_tz(some_time))
    return (datetime(1970, 1, 1) + timedelta(seconds=timestamp)).replace(tzinfo=pytz.UTC)


class Command(BaseCommand):
    help = 'Using Json file'

    def handle(self, *args, **options):
        with open('bin/activity.csv') as file2:
            activity_reader = csv.DictReader(file2)
            for activity in activity_reader:
                activity_dict = dict(activity)

                userid = Profile.objects.filter(userid=activity_dict['id']).first()
                _, created = ActivityPeriod.objects.update_or_create(
                    profile=userid,
                    start_time=conv_time(activity_dict['start_time']),
                    end_time=conv_time(activity_dict['end_time'])
                )
