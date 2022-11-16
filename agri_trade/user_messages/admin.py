from django.contrib import admin

from agri_trade.user_messages.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'body', 'created_at')
