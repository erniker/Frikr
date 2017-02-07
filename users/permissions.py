# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET,POST, PUT, DELETE)
        """
        from users.api import UserDetailAPI
        # si quiere crear un usuario, sea quien sea, debe poder
        # crearlo
        if request.method == "POST":
            return True
        # si es superuser, puede hacer lo que quiera
        elif request.user.is_superuser:
            return True
        # si no es POST ( es un GET, PUT o DELETE), el usuario no es
        # superuser y la petición va a la vista de detalle, entonces
        # lo permitimos para tomar la decisión en el método
        # has_object_permissions
        elif isinstance(view, UserDetailAPI):
            return True
        # Si la petición es un GET a listado, no lo permitiremos
        # (porque si llega aquí, el usuario no es superuser y solo
        # pueden los superuser)
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET,POST, PUT, DELETE)
        sobre el object obbj
        """
        return request.user.is_superuser or request.user == obj
