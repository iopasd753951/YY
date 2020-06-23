from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='accounts/login.html')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('signup/', TemplateView.as_view(template_name='accounts/signup.html'), name='signup'),
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login')
]
