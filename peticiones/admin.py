from django.contrib.gis import admin
from peticiones.models import Peticion, SolicitudAccesoPeticion
from emails.aux import get_url_autorizacion_peticion


class PeticionAdmin(admin.OSMGeoAdmin):
    list_display = ('nombre', 'id', 'telefono', 'email', 'creacion')
    readonly_fields = ('creacion',)


class SolicitudAccesoPeticionAdmin(admin.OSMGeoAdmin):
    def nombre_necesitado(self, obj):
        return obj.peticion.nombre

    def telefono_necesitado(self, obj):
        return obj.peticion.telefono

    def email_necesitado(self, obj):
        return obj.peticion.email

    def mensaje_necesitado(self, obj):
        return obj.peticion.mensaje

    def url_autorizacion(self, obj):
        return get_url_autorizacion_peticion(obj.codigo_acceso)

    exclude = ['peticion']
    list_display = (
        'id',
        'nombre',
        'nombre_necesitado',
        'acceso_permitido',
        'codigo_acceso',
        'creacion',
    )
    readonly_fields = (
        'codigo_acceso',
        'url_autorizacion',
        'nombre_necesitado',
        'telefono_necesitado',
        'email_necesitado',
        'mensaje_necesitado',
        'creacion'
    )
    fieldsets = (
        ('Datos de la petición', {
            'fields': (
                'nombre_necesitado',
                'telefono_necesitado',
                'email_necesitado',
                'mensaje_necesitado',
                'codigo_acceso',
                'url_autorizacion',
                'acceso_permitido',
            ),
        }),
        ("Datos del colaborador", {
            'fields': (
                'nombre',
                'telefono',
                'email',
                'mensaje',
                'creacion',
            ),
        }),
    )


admin.site.register(Peticion, PeticionAdmin)
admin.site.register(SolicitudAccesoPeticion, SolicitudAccesoPeticionAdmin)
