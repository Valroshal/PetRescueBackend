from django.contrib.admin import ModelAdmin, site

from PetRescueBackend.core.models import BaseModel


class BaseAdmin(ModelAdmin):
    empty_value_display = '---'
    list_display = ('created', 'modified', 'is_deleted',)
    list_filter = ('created', 'modified', 'is_deleted',)
    ordering = ('-modified',)

    list_per_page = 25

    @staticmethod
    def register(
            model: type(BaseModel),
            admin_class: type(ModelAdmin)
    ):
        admin_class.list_display += BaseAdmin.list_display
        site.register(model, admin_class)
