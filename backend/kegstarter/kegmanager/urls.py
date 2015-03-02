from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'beers', views.BeerViewSet)
router.register(r'brewers', views.BrewerViewSet)
urlpatterns = router.urls
