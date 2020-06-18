from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError
from django.contrib.auth import authenticate, login, logout


class BaseView(View):
    @staticmethod
    def response(data={}, message="", status=200):

        result = {
            'data': data,
            'message': message,
        }

        return JsonResponse(result, status)


class UserSignupView(BaseView):
    @method_decorator(csrf_exempt) # ajax 통신시(POST요청) CSRF 토큰요구로 에러가 발생하는데 그것을 우회함
    def dispatch(self, request, *args, **kwargs):
        return super(UserSignupView, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            self.response(message="올바른 이메일을 입력해주세요.", status=400)

        user_name = request.POST.get('user_name', '')
        if not user_name:
            return self.response(message="이름을 입력해주세요.", status=400)

        password = request.POST.get('password', '')
        if not password:
            return self.response(message="비밀번호를 입력해주세요.", status=400)

        phone_number = request.POST.get('phone_number', status=400)
        if not phone_number:
            return self.response(message="휴대폰번호를 입력해주세요.")

        try:
            user = User.objects.create_user(user_name, password, email, phone_number)
        except IntegrityError:
            return self.response(message="이미 존재하는 아이디입니다. 새로 만들어주세요.", status=400)

        return self.response({'user.id': user.id})


class UserLoginView(BaseView):
    def post(self, request):
        email = request.POST.get('email', '')
        if not email:
            return self.response(message="email을 입력해주세요", status=400)

        password = request.POST.get('password', '')
        if not password:
            return self.response(message="비밀번호를 입력해주세요.", status=400)

        user = authenticate(request, email=email, password=password) # authenticate() 는 값이 들어오지않으면 None값을 반환한다.
        if user is None:
            return self.response(message="입력정보를 확인해주세요", status=400)

        login(request, user)

        return self.response


class UserLogoutView(BaseView):
    def get(self, request):
        logout(request)
        return self.response()