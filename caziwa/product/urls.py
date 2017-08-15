from django.conf.urls import include, url
from product.views import category_view, cataloge_view,product_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^category/(?P<category_slug>[\w\-]+)/$', category_view, name='category'),
    url(r'^subcategory/(?P<category_slug>[\w\-]+)/(?P<subcategory_slug>[\w\-]+)/$', cataloge_view, name='subcategory'),
    url(r'^product/(?P<category_slug>[\w\-]+)/(?P<subcategory_slug>[\w\-]+)/(?P<product_id>\d+)/$',
        product_view, name='product'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)