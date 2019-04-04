from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me': "HELLO I AM FROM views.py !!"}
    return render(request, 'testproject_app\index.html', context=my_dict)
