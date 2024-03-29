"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from article.views import home
from article.views import detail
from article.views import create
from cssapayment.views import paymentdetail
from cssapayment.views import createpayment
from cssapayment.views import totalpayment
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/(?P<pk>[0-9]+)/$', detail),
    url(r'^article/create/$', create),
    url(r'^payment/(?P<pk>[0-9]+)/$', paymentdetail),
    url(r'^payment/create/$', createpayment),
    url(r'^payment/total/$', totalpayment),
    url(r'^$', home),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
