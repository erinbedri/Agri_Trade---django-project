from django.shortcuts import get_object_or_404

from agri_trade.posts.models import Post, PostComment


def get_all_posts():
    return Post.objects.all()


def get_single_post(pk):
    return get_object_or_404(Post, pk=pk)


def get_all_comments(pk):
    return PostComment.objects\
        .filter(post_id__exact=pk)\
        .order_by('created_on')


