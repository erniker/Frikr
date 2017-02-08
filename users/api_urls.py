# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from users.api import UserViewSet
from rest_framework.routers import DefaultRouter


# API Router
router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
   # API URLs
    url(r'1.0/', include(router.urls)),   # incluyo las URLS de API
]
