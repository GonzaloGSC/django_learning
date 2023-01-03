from django.urls import path, re_path, include
from apps.matches import views

urlpatterns = [
    path('matches/', include([
        path('team', views.v_team.as_view()),
    ])),
]