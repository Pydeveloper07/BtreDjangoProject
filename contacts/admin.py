from django.contrib import admin
from .models import Contact

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'email', 'phone')
    list_per_page = 25

admin.site.register(Contact, ContactsAdmin)
