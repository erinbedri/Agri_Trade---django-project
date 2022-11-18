from django.shortcuts import get_object_or_404

from agri_trade.posts.models import Post, PostComment


def get_all_posts():
    posts = Post.objects.all()
    return posts


def get_single_post(pk):
    post = get_object_or_404(Post, pk=pk)
    return post


def get_all_comments(pk):
    comments = PostComment.objects\
        .filter(post_id__exact=pk)\
        .order_by('created_on')
    return comments


