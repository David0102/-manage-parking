from django.urls import path
from reserva import views

urlpatterns = [
    path('', views.ReservaListView.as_view(), name='reservas'),
    path('cadastro/', views.cadastrar_reserva, name='cadastrar_reserva'),
    path('finalizar/<int:id>', views.finalizar_reserva, name='finalizar_reserva'),
    path('confirm_delete/<int:id>', views.confirm_delete, name='confirm_delete'),
    path('deletar/', views.deletar_reserva, name='deletar_reserva'),
    path('busca/', views.busca_reserva, name='busca_reserva'),
]
