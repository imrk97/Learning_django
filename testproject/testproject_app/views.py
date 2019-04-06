from django.shortcuts import render
from django.http import HttpResponse
from testproject_app.models import Topic, Webpage, AccessRecord
# Create your views here.


def index(request):
    webpages_list=Webpage.objects
    date_dict={'access_record':webpages_list}
    #my_dict = {'insert_me': "HELLO I AM FROM views.py !!"}
    return render(request, 'testproject_app\index.html', context=date_dict)
