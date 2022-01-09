from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),

    # path('contact',views.contact,name='contact'),
    path('instructors',views.instructors,name='instructors'),
    path('booking',views.booking,name='booking'),
    path('reserve',views.reserve,name='reserve'),
    path('post',views.post,name='post'),

]
