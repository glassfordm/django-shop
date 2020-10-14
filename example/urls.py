from django.conf.urls import include, url
from example.myshop.views import MyOrderConfirmView

from shop import urls as shop_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^checkout/confirm/$', MyOrderConfirmView.as_view(), name='checkout_shipping'),
    url(r'^', include(shop_urls)), # <-- That's the important bit
]
