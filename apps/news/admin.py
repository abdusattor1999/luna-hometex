from django.contrib import admin
from .models import News, Product, Message


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at')
    list_display_links = list_display

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    list_display_links = list_display

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', "status", 'created_at')
    list_display_links = list_display