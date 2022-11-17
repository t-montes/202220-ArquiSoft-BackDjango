from django.contrib import admin
from django.urls import include, path, re_path
from . import views
from django.views.static import serve
from django.conf import settings


static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('health-check/', views.healthCheck),
    path('', include('documentos.urls')),
    path('formato/', include('formato.urls')),
    path('celda/', include('celda.urls')),
    path('creditos/', include('creditos.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
    path("", include(static_urlpatterns))
]
