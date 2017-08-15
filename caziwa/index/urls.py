from django.conf.urls import url
from .views import home
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', home, name='home'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)