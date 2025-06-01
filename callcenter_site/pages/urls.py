# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',        views.home,     name='home'),      # "/" 요청 시 home 뷰
    path('services/', views.services, name='services'),
    path('process/',  views.process,  name='process'),
    path('advantages/', views.advantages, name='advantages'),
    path('pricing/',  views.pricing,  name='pricing'),
    path('faq/',      views.faq,      name='faq'),
]