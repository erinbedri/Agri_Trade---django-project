from django.contrib import admin

from agri_trade.user_messages.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('body', 'sender', 'receiver', 'subject', 'created_at', 'is_read')

    search_fields = ['body', 'sender__username', 'receiver__username', 'subject', 'created_at', 'is_read']
    list_filter = ('is_read', )
