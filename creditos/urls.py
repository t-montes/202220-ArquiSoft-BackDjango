from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include
from . import views
urlpatterns = [
    path('creditoupdate/', csrf_exempt(views.credito_update), name='creditoUpdate'),
    path('creditocreate/', csrf_exempt(views.credito_create), name='creditoCreate'),
    path('creditos/', csrf_exempt(views.creditos_list), name='creditosList'),
    path('credito/<int:id>/', csrf_exempt(views.credito_detail), name='creditoDetail'),
]
