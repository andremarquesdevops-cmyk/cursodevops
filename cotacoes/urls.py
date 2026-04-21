from django.urls import path

from .views import CadastroCotacaoView, LoginVendedorView, LogoutVendedorView, PainelCotacoesView

urlpatterns = [
    path('', CadastroCotacaoView.as_view(), name='cadastro_cotacao'),
    path('login/', LoginVendedorView.as_view(), name='login_vendedor'),
    path('painel/', PainelCotacoesView.as_view(), name='painel_cotacoes'),
    path('sair/', LogoutVendedorView.as_view(), name='logout_vendedor'),
]
