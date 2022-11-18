from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from agri_trade.posts.forms import PostCommentForm
from agri_trade.posts import services as post_services


def show_posts(request):
    posts = post_services.get_all_posts()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/show_posts.html', context)


def show_post(request, pk):
    post = post_services.get_single_post(pk=pk)
    comments = post_services.get_all_comments(pk=pk)
    comments_count = comments.count()

    context = {
        'post': post,
        'comments': comments,
        'comments_count': comments_count,
    }

    return render(request, 'posts/show_post.html', context)


def show_comments(request, pk):
    post = post_services.get_single_post(pk=pk)
    comments = post_services.get_all_comments(pk=pk)
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
