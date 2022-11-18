from django.shortcuts import get_object_or_404

from agri_trade.marketplace.models import Product
from agri_trade.user_messages.models import Message


def get_all_inbox_messages(user):
    messages = Message.objects \
        .filter(receiver=user) \
        .order_by('-created_at')
    return messages


def get_all_outbox_messages(user):
    messages = Message.objects \
        .filter(sender=user) \
        .order_by('-created_at')
    return messages


def get_single_message(pk):
    message = get_object_or_404(Message, pk=pk)
    return message


def get_single_product(pk):
    product = get_object_or_404(Product, pk=pk)
    return product


def get_owner_of_single_product(pk):
    owner = get_single_product(pk).owner
    return owner


