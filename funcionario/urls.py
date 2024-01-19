from django.urls import path
from funcionario import views

urlpatterns = [
    path('', views.funcionarios, name='funcionarios'),
    path('cadastro/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('editar/<int:pk>', views.editar_funcionario_get, name='editar_funcionario_get'),
    path('editar/', views.editar_funcionario_post, name='editar_funcionario_post'),
    path('excluir/<int:pk>', views.FuncionarioDeleteView.as_view(), name='deletar_funcionario'),
    path('change_password_get/<int:id>', views.change_password_get, name='change_password_get'),
    path('change_password_post', views.change_password_post, name='change_password_post'),
    path('busca/', views.busca_funcionario, name='busca_funcionario'),
]