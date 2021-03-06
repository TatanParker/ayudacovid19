from colaboradores import views as colaboradores_views
from colaboradores import views_rest as colaboradores_rest

from rest_framework import routers
from django.urls import path

urlpatterns = [
    path('colaboradores/add', colaboradores_views.CrearColaboradorView.as_view(), name='crear-colaborador'),
    path('colaboradores/<pk>/acceso', colaboradores_views.SolicitarContactoColaboradorView.as_view(), name='acceso-colaborador'),
    path('colaboradores/validar', colaboradores_views.permitirContacto, name='validar-acceso-colaborador'),
    path('API/colaboradores/solicitudes', colaboradores_views.solicitudes, name="solicitudes-colaborador")
]

router = routers.SimpleRouter()
router.register('API/colaboradores', colaboradores_rest.APIColaboradoresView)
router.register('API/colaboradores/acceso', colaboradores_rest.APIContactoColaboradorView)

urlpatterns += router.urls
