from django.urls import path, include

from accounts.views import UserSignupView, UserLoginView, UserLogoutView, UserMypageView

urlpatterns = [
    path('v1/signup', UserSignupView.as_view(), name="v1_user_signup"),
    path('v1/login', UserLoginView.as_view(), name="v1_user_login"),
    path('v1/loguot', UserLogoutView.as_view(), name="v1_user_logout"),

    path('v1/mypage', UserMypageView.as_view(), name="v1_user_mypage"),
]
