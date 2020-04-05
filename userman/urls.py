from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userman import views

urlpatterns = [
    path('profile/', views.ProfileList.as_view()),
    path('activity', views.ActivityPeriodList.as_view()),
    path('user', views.UserList.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
