from django.contrib import admin

from agri_trade.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'created_on')
