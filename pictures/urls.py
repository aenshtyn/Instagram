from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
 
    url('account/', include('django.contrib.auth.urls')),
    url('',views.index,name = 'index'),
    url('^$',views.login,name = 'login'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)