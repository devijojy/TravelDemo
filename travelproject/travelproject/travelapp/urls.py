from.import views
from django.urls import path

urlpatterns = [

     path('',views.demo,name='demo'),
    #path('about/',views.about,name='about'),
    #path('value',views.value,name='value'),
    #path('', views.value, name='value'),
    #path('add/',views.addition,name='addition')


]
