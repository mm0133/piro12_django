from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'is_publish']
    list_display_links = ['name']
    list_filter = ['is_publish', 'updated_at']
    search_fields = ['name']

def short_des(self,item):
    return item.desc[:20]

# Register your models here.
