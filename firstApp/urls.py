
from django.urls import path
from firstApp import views
urlpatterns = [
    path('wish/', views.wish),
]
