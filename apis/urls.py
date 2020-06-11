from django.urls import path, include

from apis import views

urlpatterns = [
    path('v1/users/create', views.UserCreateView.as_view(), name='apis_v1_user_create'),
    path('v1/users/login', views.UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/users/logout', views.UserLogoutView.as_view(), name='apis_v1_user_logout'),
]
