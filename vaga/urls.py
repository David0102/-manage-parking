from django.urls import path
from vaga import views

urlpatterns = [
    path('', views.VagaListView.as_view(), name='vagas'),
    path('cadastrar/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('confirm_delete/<int:id>', views.confirm_delete_vaga, name='confirm_delete_vaga'),
    path('deletar/', views.deletar_vaga, name='deletar_vaga'),
]
