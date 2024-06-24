from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/archivos', ArchivosViewSet, 'archivos')
router.register('api/region', RegionViewSet, 'region')
router.register('api/provincia', ProvinciaViewSet, 'provincia')
router.register('api/comuna', ComunaViewSet, 'comuna')
router.register('api/Area', AreaViewSet, 'Area')
router.register('api/Cliente', ClienteViewSet, 'Cliente')
router.register('api/Depto', DeptoViewSet, 'Depto')
router.register('api/Deptoempresa', DeptoempresaViewSet, 'Deptoempresa')
router.register('api/Empresa', EmpresaViewSet, 'Empresa')
router.register('api/Estado', EstadoViewSet, 'Estado')
router.register('api/Logestadoticket', LogestadoticketViewSet, 'Logestadoticket')
router.register('api/Mensajes', MensajesViewSet, 'Mensajes')
router.register('api/Permisos', PermisosViewSet, 'Permisos')
router.register('api/Prioridad', PrioridadViewSet, 'Prioridad')
router.register('api/Rol', RolViewSet, 'Rol')
router.register('api/Rolpermiso', RolpermisoViewSet, 'Rolpermiso')
router.register('api/Tecnico', TecnicoViewSet, 'Tecnico')
router.register('api/Tecticket', TecticketViewSet, 'Tecticket')
router.register('api/Ticketarea', TicketareaViewSet, 'Ticketarea')
router.register('api/Tipoticket', TipoticketViewSet, 'Tipoticket')
router.register('api/User', UserViewSet, 'User')

urlpatterns = router.urls