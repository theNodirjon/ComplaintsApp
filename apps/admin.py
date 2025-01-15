from django.contrib import admin

from apps.models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'text')
