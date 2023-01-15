from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import re_path, reverse
from django.utils.html import format_html

from PetRescueBackend.core.admin import BaseAdmin
from PetRescueBackend.user.models import User


class UserAdmin(BaseAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'password'
    )
    search_fields = ('id', 'first_name', 'last_name', 'email',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            re_path(
                r'^(?P<pk_id>.+)/user_info/$',
                self.admin_site.admin_view(self.user_info_action),
                name='user_info_action',
            ),
        ]
        return custom_urls + urls

    def user_info(self, obj):
        return format_html(
            '<a class="button" href="{}">Info</a>',
            reverse(
                'admin:user_info_action',
                args=[obj.pk]
            ),
        )

    def user_info_action(self, obj, pk_id):
        return HttpResponseRedirect(f'/user/ui/info/{pk_id}')


# BaseAdmin.register(User, UserAdmin)
admin.site.register(User, UserAdmin)
