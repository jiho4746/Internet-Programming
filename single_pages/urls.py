from django.urls import path
from . import views

urlpatterns = [ #서버IP/
    path('', views.landging), #서버IP/
    path('about_me/', views.about_me) #서버IP/about_me
]