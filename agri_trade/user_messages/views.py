from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from agri_trade.marketplace.models import Product
from agri_trade.user_messages.forms import SendMessageForm
from agri_trade.user_messages.models import Message


@login_required
def show_messages(request):
    messages_inbox = Message.objects\
        .filter(receiver=request.user)\
        .order_by('-created_at')

    messages_outbox = Message.objects\
        .filter(sender=request.user)\
        .order_by('-created_at')

    unread_messages_count = Message.objects\
        .filter(is_read=False)\
        .filter(receiver=request.user)\
        .count()

    context = {
        'messages_inbox': messages_inbox,
        'messages_outbox': messages_outbox,
        'unread_messages_count': unread_messages_count,
    }

    return render(request, 'user_messages/messages.html', context)


@login_required
def show_message(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    if not msg.is_read:
        msg.is_read = True
        msg.save()

    context = {
        'message': msg,
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
