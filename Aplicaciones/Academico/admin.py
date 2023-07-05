from django.contrib import admin
from .models import Curso

# Register your models here.

#admin.site.register(Curso)
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','creditos')
    search_fields = ('nombre', 'creditos')