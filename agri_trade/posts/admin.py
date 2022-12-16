from django.contrib import admin

from agri_trade.posts.models import Post, PostComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')

    search_fields = ['title', 'author__username', 'created_on']
    list_filter = ('author', )


@admin.register(PostComment)
class PostComment(admin.ModelAdmin):
    list_display = ('author', 'post', 'body', 'created_on')