from rest_framework.routers import DefaultRouter
from invetario.api.views import ProductoViewSet


router = DefaultRouter()
router.register('productos', ProductoViewSet,basename='productos')

urlpatterns = router.urls