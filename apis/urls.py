from django.urls import path, include

from apis import views

urlpatterns = [
    path('v1/users/signup', views.UserSignupView.as_view(), name='apis_v1_user_signup'),
    path('v1/users/login', views.UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/users/logout', views.UserLogoutView.as_view(), name='apis_v1_user_logout'),
]
