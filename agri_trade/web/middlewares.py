from django.utils.deprecation import MiddlewareMixin

from agri_trade.user_messages.models import Message


class GetUnreadMessagesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        unread_messages_count = Message.objects\
            .filter(receiver=request.user)\
            .filter(is_read=False)\
            .count()
        request.unread_messages_count = unread_messages_count
