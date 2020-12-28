from django.contrib import admin

from .models import Persona,Publicacion,Comment

# Register your models here.
admin.site.register(Persona)
admin.site.register(Publicacion)
admin.site.register(Comment)
