from django.contrib import admin
from userman.models import Profile, ActivityPeriod


# admin.site.register(Profile)
# admin.site.register(ActivityPeriod)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'timezone')


admin.site.register(Profile, ProfileAdmin)


class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('profile', 'start_time', 'end_time')


admin.site.register(ActivityPeriod, ActivityPeriodAdmin)