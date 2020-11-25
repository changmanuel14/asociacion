# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from asociados.models import Asociado, Especialidad, Subespecialidad

# Register your models here.

admin.site.register(Asociado)
admin.site.register(Especialidad)
admin.site.register(Subespecialidad)
