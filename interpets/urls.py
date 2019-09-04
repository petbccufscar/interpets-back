from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from interpets2019 import views

router = routers.DefaultRouter()
router.register(r'petiano', views.PetianoViewSet)
router.register(r'gdt', views.GDTViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/admin/', admin.site.urls),
]
