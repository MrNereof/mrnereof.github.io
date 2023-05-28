from django.contrib import admin
from web.models import Painting, Project


@admin.register(Painting, Project)
class BaseAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
