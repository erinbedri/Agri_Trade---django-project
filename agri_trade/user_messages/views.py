from django.shortcuts import render, get_object_or_404

from agri_trade.user_messages.models import Message


def messages(request):
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


def message(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    context = {
        'message': msg,
    }

    return render(request, 'user_messages/message.html', context)
