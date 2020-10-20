from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)

admin.site.register(Certificate, CertificateAdmin)
