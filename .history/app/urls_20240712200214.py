from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('archivos', ArchivosViewSet, 'archivos')
router.register('region', RegionViewSet, 'region')
router.register('provincia', ProvinciaViewSet, 'provincia')
router.register('comuna', ComunaViewSet, 'comuna')
router.register('area', AreaViewSet, 'Area')
router.register('cliente', ClienteViewSet, 'Cliente')
router.register('depto', DeptoViewSet, 'Depto')
router.register('empresa', EmpresaViewSet, 'Empresa')
router.register('estado', EstadoViewSet, 'Estado')
router.register('ticket', TicketViewSet, 'Ticket')
router.register('logestadoticket', LogestadoticketViewSet, 'Logestadoticket')
router.register('mensajes', MensajesViewSet, 'Mensajes')
router.register('permisos', PermisosViewSet, 'Permisos')
router.register('prioridad', PrioridadViewSet, 'Prioridad')
router.register('rol', RolViewSet, 'Rol')
router.register('rolpermiso', RolpermisoViewSet, 'Rolpermiso')
router.register('tecnico', TecnicoViewSet, 'Tecnico')
router.register('tecticket', TecticketViewSet, 'Tecticket')
router.register('ticketarea', TicketareaViewSet, 'Ticketarea')
router.register('tipoticket', TipoticketViewSet, 'Tipoticket')
router.register('user', UserViewSet, 'User')
router.register('ticketpost', TicketViewSet.perform_create, 'ticketpost')

urlpatterns = router.urls