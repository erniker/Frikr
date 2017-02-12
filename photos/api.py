#-*- coding: utf-8 -*-
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from photos.views import PhotosQueryset
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter


class PhotoViewSet(PhotosQueryset, ModelViewSet):
    """
    Este Viewset hace lo mismo que las clases PhotoListAPI y PhotoDetail API
    pero en una sola clase
    """
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filter_backends = (SearchFilter, OrderingFilter)
    search_field = ('name', 'description', 'owner__first_name')
    ordering_fields = ('name', 'owner')

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de la nueva foto al usuario
        autenticado
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.get_photos_queryset(self.request)