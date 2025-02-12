from django.urls import path
from testapp import views

urlpatterns = [
    
    path('', views.test_view ),
]