from django.urls import path, include

from accounts.views import UserSignupView, UserLoginView

urlpatterns = [
    path('v1/signup', UserSignupView.as_view(), name="v1_user_signup"),
    path('v1/login', UserLoginView.as_view(), name="v1_user_login"),
]
