from rest_framework.routers import SimpleRouter
from .views import *
router = SimpleRouter()
router.register(r"category",CategoryCURD,basename="category")
router.register(r"product",ProductCURD,basename="product")
urlpatterns = [
    
]+router.urls
