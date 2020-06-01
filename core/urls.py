from django.urls import path

# . = core
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),  # name é o nome da rota
    path('contato', contato, name='contato' ),
    path('produto/<int:pk>', produto, name='produto')
]

