from django.urls import path
from basicapp import views

 #TEMPLATE TAGGING
app_name = 'basicapp'
urlpatterns =[
     path(r'relative/',views.relative,name='relative'),
     path(r'other/',views.other,name='other'),
 ]
