from rest_framework import viewsets
from rest_framework import mixins
from peticiones.models import Peticion
from peticiones.models import SolicitudAccesoPeticion
from peticiones.serializers import PeticionSerializer
from peticiones.serializers import PeticionListSerializer
from peticiones.serializers import SolicitudAccesoPeticionSerializer
from fuentes.api import actualizar_fuente
from emails.emails import enviar_correo_nueva_peticion
from emails.emails import enviar_correo_ofreciendo_ayuda
from emails.emails import enviar_correo_nueva_solicitud_peticion


class APIPeticionesView(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Peticion.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return PeticionSerializer
        return PeticionListSerializer

    def perform_create(self, serializer):
        if "key" in self.request.data:
            actualizar_fuente(self.request.data["key"])
        serializer.save()
        enviar_correo_nueva_peticion.delay()


class APIContactarPeticionView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SolicitudAccesoPeticion.objects.all()
    serializer_class = SolicitudAccesoPeticionSerializer

    def perform_create(self, serializer):
        if "key" in self.request.data:
            actualizar_fuente(self.request.data["key"])
        contacto = serializer.save()
        enviar_correo_nueva_solicitud_peticion.delay()
        enviar_correo_ofreciendo_ayuda.delay(contacto.pk)
