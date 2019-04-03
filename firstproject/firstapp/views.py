from django.shortcuts import render

# Create your views here.
def index(request):
    mydict={'insert_content':"hello im from firstapp!!"}
    return render(request,'firstapp/index.html',context=mydict)