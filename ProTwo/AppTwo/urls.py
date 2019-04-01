
from django.urls import path
from AppTwo import views
urlpatterns = [
    path('',views.index,name='anything'),
    #path('admin/', admin.site.urls),
]