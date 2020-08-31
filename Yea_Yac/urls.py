from . import settings

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', TemplateView.as_view(template_name='accounts/login.html')),
    path('admin/', admin.site.urls),

    path('account/', include('accounts.urls')),
    path('store/', include('store.urls')),

    path('signup/', TemplateView.as_view(template_name='accounts/signup.html'), name='signup'),
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', TemplateView.as_view(template_name='accounts/logout.html'), name='logout'),

    path('main/', TemplateView.as_view(template_name='store/main.html'), name='main'),
    path('main/search/', TemplateView.as_view(template_name='store/header.html'), name='search'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
