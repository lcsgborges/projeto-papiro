from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notas, name='listar_nota'),
    path('criar', views.criar_nota, name='criar_nota')  
]
