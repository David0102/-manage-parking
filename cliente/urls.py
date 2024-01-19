from django.urls import path
from cliente import views

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='clientes'),
    path('cadastro/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('excluir/<int:pk>', views.ClienteDeleteView.as_view(), name='deletar_cliente'),
    path('editar/<int:pk>', views.editar_cliente_get, name='editar_cliente_get'),
    path('editar/', views.editar_cliente_post, name='editar_cliente_post'),
    path('busca/', views.busca_cliente, name='busca_cliente'),
]
