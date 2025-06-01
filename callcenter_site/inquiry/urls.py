# inquiry/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),  # "/contact/" 요청 시 contact 뷰
]