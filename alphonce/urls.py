from django.urls import path
from alphonce import views

urlpatterns = [
    path("", views.home, name='home'),
    path('/index/', views.index, name='index'),
    path("/detail/", views.detail, name='detail'),
]