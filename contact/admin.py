from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created_at")
    search_fields = ("name", "email", "company", "phone", "service", "message")
    list_filter = ("service", "created_at")

# Register your models here.
