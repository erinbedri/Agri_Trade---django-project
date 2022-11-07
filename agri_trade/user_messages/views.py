from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from agri_trade.marketplace.models import Product
from agri_trade.user_messages.forms import SendMessageForm, DeleteMessageForm, ReplyMessageForm
from agri_trade.user_messages.models import Message


@login_required
def show_messages(request):
    messages_inbox = Message.objects\
        .filter(receiver=request.user)\
        .order_by('-created_at')

    messages_outbox = Message.objects\
        .filter(sender=request.user)\
        .order_by('-created_at')

    context = {
        'messages_inbox': messages_inbox,
        'messages_outbox': messages_outbox,
    }

    return render(request, 'user_messages/messages.html', context)


@login_required
def show_message(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if not message.is_read and message.receiver == request.user:
        message.is_read = True
        message.save()

    context = {
        'message': message,
    }

    return render(request, 'user_messages/message.html', context)


@login_required
def send_message(request, pk):
    owner = get_object_or_404(Product, pk=pk).owner
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = owner
            message.subject = request.POST['subject']
            message.body = request.POST['body']
            message.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('marketplace:marketplace')
        else:
            messages.error(request, "Your message couldn't be sent.")
    else:
        form = SendMessageForm({'receiver': owner})

    context = {
        'owner': owner,
        'product': product,
        'form': form,
    }

    return render(request, 'user_messages/send_message.html', context)


@login_required
def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.method == 'POST':
        form = DeleteMessageForm(request.POST, instance=message)
        if form.is_valid():
            message.delete()
            messages.success(request, 'Your message was deleted successfully!')
            return redirect('user_messages:messages')
        else:
            messages.error(request, 'Your message couldn\'t be deleted! Try again later.')
    else:
        form = DeleteMessageForm()

    context = {
        'message': message,
        'form': form,
    }

    return render(request, 'user_messages/delete_message.html', context)


@login_required
def reply_message(request, pk):
    reply_to_message = get_object_or_404(Message, pk=pk)
    reply_to_user = reply_to_message.sender

    if request.method == 'POST':
        form = ReplyMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = reply_to_user
            message.subject = f'Re: {reply_to_message.subject}'
            message.body = request.POST['body']
            message.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('user_messages:messages')
        else:
            messages.error(request, "Your message couldn't be sent.")
    else:
        form = ReplyMessageForm({'receiver': reply_to_user})

    context = {
        'reply_to_user': reply_to_user,
        'reply_to_message': reply_to_message,
        'form': form,
    }

    return render(request, 'user_messages/reply_to_message.html', context)