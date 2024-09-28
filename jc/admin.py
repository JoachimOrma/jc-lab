from django.contrib import admin
from .models import Guest

# Register your models here.
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    search_fields = ['email', 'name', 'phone']