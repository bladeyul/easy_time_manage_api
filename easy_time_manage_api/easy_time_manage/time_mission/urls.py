from django.urls import path

from . import views

urlpatterns=[
    path('now',view.now_mission),
    path('next',view.next_mission),
    path('delay',view.delay_mission),
]
