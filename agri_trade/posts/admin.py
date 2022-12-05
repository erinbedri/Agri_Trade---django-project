from django.contrib import admin

from agri_trade.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author__username', 'created_on']
    list_display = ('title', 'author', 'created_on')
