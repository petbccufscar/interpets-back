from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from evento import views

router = routers.DefaultRouter()
router.register(r'petiano', views.PetianoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('petufscar/api/', include(router.urls)),
    path('petufscar/api/admin/', admin.site.urls),
]
