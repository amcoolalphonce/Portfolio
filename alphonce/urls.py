from django.urls import path
from alphonce import views

urlpatterns = [
    path("", views.home, name='home'),
]