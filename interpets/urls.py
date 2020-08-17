from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from evento import views

router = routers.DefaultRouter()
router.register(r'petiano', views.PetianoViewSet, basename='Petiano')
router.register(r'gdt', views.GDTViewSet, basename='GDT')
router.register(r'gdt_disp', views.GDTDisponivelViewSet, basename='GDT_disp')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('petufscar/api/', include(router.urls)),
    path('petufscar/api/admin/', admin.site.urls),
]
