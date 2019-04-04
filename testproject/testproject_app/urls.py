from django.urls import path
from testproject_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
