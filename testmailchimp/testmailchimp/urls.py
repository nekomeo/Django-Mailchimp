from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from api import views as api


router = routers.DefaultRouter()
router.register(r'contact', api.ContactViewSet, base_name='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
