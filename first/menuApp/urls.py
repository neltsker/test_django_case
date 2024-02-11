
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainView, name='main'),
    path('<path:path>/', views.SubView, name='submenu'),
]