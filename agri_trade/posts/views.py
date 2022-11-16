from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from agri_trade.posts.forms import PostCommentForm
from agri_trade.posts.models import Post, PostComment


def show_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/show_posts.html', context)


def show_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = PostComment.objects \
        .filter(post_id__exact=pk) \
        .order_by('created_on')
    comments_count = comments.count()

    context = {
        'post': post,
        'comments_count': comments_count,
    }

    return render(request, 'posts/show_post.html', context)


def show_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = PostComment.objects \
        .filter(post_id__exact=pk) \
        .order_by('created_on')
    comments_count = comments.count()

    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('posts:show comments', args=[str(pk)]))
    else:
        form = PostCommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comments_count': comments_count,
        'form': form,
    }

    return render(request, 'posts/show_comments.html', context)
