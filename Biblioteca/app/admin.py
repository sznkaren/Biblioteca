from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
admin.site.register(Cidade)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)