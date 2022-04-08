from django.urls import path
from .views import Home,ProfileList,ProfileCreate

app_name = 'core'

urlpatterns=[
    path('',Home.as_view()),
    path('profile/',ProfileList.as_view(),name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(),name='profile_create'),
]