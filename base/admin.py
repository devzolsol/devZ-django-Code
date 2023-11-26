from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'phone', 'email', 'is_mailed']
    list_filter = ['is_mailed']
    search_fields = ['name', 'company_name', 'phone', 'email', 'phone', 'address_phone']