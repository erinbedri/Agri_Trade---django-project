from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from agri_trade.user_messages.forms import SendMessageForm, DeleteMessageForm, ReplyMessageForm
from agri_trade.user_messages import services as user_messages_services

SEND_MESSAGE_SUCCESS_MESSAGE = 'Your message was successfully sent!'
SEND_MESSAGE_ERROR_MESSAGE = 'Your message couldn\'t be sent.'

DELETE_MESSAGE_SUCCESS_MESSAGE = 'Your message was deleted successfully!'
DELETE_MESSAGE_ERROR_MESSAGE = 'Your message couldn\'t be deleted! Try again later.'


@login_required
def show_messages(request):
    messages_inbox = user_messages_services.get_all_inbox_messages(user=request.user)
    messages_outbox = user_messages_services.get_all_outbox_messages(user=request.user)

    context = {
        'messages_inbox': messages_inbox,
        'messages_outbox': messages_outbox,
    }

    return render(request, 'user_messages/messages.html', context)


@login_required
def show_message(request, pk):
    message = user_messages_services.get_single_message(pk)

    if not message.is_read and message.receiver == request.user:
        message.is_read = True
        message.save()

    context = {
        'message': message,
    }

    return render(request, 'user_messages/message.html', context)


@login_required
def send_message(request, pk):
    product = user_messages_services.get_single_product(pk)
    owner = product.owner

    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = owner
            message.subject = request.POST['subject']
            message.body = request.POST['body']
            message.save()
            messages.success(request, SEND_MESSAGE_SUCCESS_MESSAGE)
            return redirect('marketplace:marketplace')
        else:
            messages.error(request, SEND_MESSAGE_ERROR_MESSAGE)
    else:
        form = SendMessageForm({'receiver': owner})

    context = {
        'product': product,
        'owner': owner,
        'form': form,
    }

    return render(request, 'user_messages/send_message.html', context)


@login_required
def delete_message(request, pk):
    message = user_messages_services.get_single_message(pk)

    if request.method == 'POST':
        form = DeleteMessageForm(request.POST, instance=message)
        if form.is_valid():
            message.delete()
            messages.success(request, DELETE_MESSAGE_SUCCESS_MESSAGE)
            return redirect('user_messages:messages')
        else:
            messages.error(request, DELETE_MESSAGE_ERROR_MESSAGE)
    else:
        form = DeleteMessageForm()

    context = {
        'message': message,
        'form': form,
    }

    return render(request, 'user_messages/delete_message.html', context)


@login_required
def reply_message(request, pk):
    reply_to_message = user_messages_services.get_single_message(pk)
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
            messages.success(request, SEND_MESSAGE_SUCCESS_MESSAGE)
            return redirect('user_messages:messages')
        else:
            messages.error(request, SEND_MESSAGE_ERROR_MESSAGE)
    else:
        form = ReplyMessageForm({'receiver': reply_to_user})

    context = {
        'reply_to_user': reply_to_user,
        'reply_to_message': reply_to_message,
        'form': form,
    }

    return render(request, 'user_messages/reply_to_message.html', context)

