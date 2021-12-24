from django.urls import path
from . import views
app_name="basicC"
urlpatterns = [
    path('templates/', views.basicD_template, name='basicD_template'),
    path('templates/basicD_form_show', views.basicD_form_show, name='basicD_form_show'),
    path('templates/basicD_form', views.basicD_form, name='basicD_form'),
    path('templates/basicD_form_show2', views.basicD_form_show2, name='basicD_form_show2'),
    path('templates/basicD_form2', views.basicD_form2, name='basicD_form2'),
    path('templates/basicD_form_show3', views.basicD_form_show3, name='basicD_form_show3'),
    path('templates/basicD_form_show4', views.basicD_form_show4, name='basicD_form_show4'),
    path('templates/basicD_form4', views.basicD_form4, name='basicD_form4'),
]