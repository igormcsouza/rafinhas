"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', views.ClienteView)
router.register('carro', views.CarroView)
router.register('defeito', views.DefeitoView)
router.register('servico', views.ServicoView)
router.register('operacao', views.OperacaoView)
router.register('transacao', views.TransacaoView)
router.register('pagamento', views.PagamentoView)
router.register('forma-de-pagamento', views.FormaDePagamentoView)
router.register('retirada', views.RetiradaView)
router.register('funcionario', views.FuncionarioView)

urlpatterns = [
    path('', include(router.urls))
]