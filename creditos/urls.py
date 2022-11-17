from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include
from . import views
urlpatterns = [
    path('creditoupdate/', csrf_exempt(views.credito_update), name='creditoUpdate'),
    path('',views.esta_funcionando_papi(), name='estaFuncionandoPapi')
]
