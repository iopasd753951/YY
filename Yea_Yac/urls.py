from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from contents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('apis/', include('apis.urls')),
    path('', views.HomeView.as_view(), name='contents_home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
]
