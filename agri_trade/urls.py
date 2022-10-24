from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('agri_trade.web.urls', 'agri_trade.web'), namespace='web')),
    path('accounts/', include(('agri_trade.accounts.urls', 'agri_trade.accounts'), namespace='accounts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
