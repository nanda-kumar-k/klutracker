from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='index'),
    path('save/', views.SaveStudent, name='save'),
    path('updateprofile/', views.UpdateStudent, name='update'),
    
]