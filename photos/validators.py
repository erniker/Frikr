#-*- coding: utf-8 -*-
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


def badwords_detector(value):
    """
    Valida si en la value se han puesto tacos definidos en settings.BADWORDS
    :return: Boolean
    """
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError(u'La palabra {0} no esta permitida'.format(badword))

    # Si todo va OK, devuelvo True
    return True
