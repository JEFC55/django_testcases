from django.urls import path
from . import views
urlpatterns = [
    path( 'bom-dia/', views.saudacao, name='saudacao')
]