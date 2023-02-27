from django.urls import path
from . import views

# import the views.py file
urlpatterns=[
    path('',views.mysite_view, name='mysite_view'),
    path('add/', views.mysite_form, name="mysite_form"),
]
