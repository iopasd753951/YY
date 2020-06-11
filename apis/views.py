from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db import IntegrityError


class BaseView(View):
    @staticmethod
    def response(data={}, message="", status=200):

        result = {
            'data': data,
            'message': message,
        }

        return JsonResponse(result, status)


class UserCreateView(BaseView):
    @method_decorator(csrf_exempt) # ajax 통신시(POST요청) CSRF 토큰요구로 에러가 발생하는데 그것을 우회함
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        user_name = request.POST.get('user_name', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number')

        user = User.objects.create_user(user_name, password, email, phone_number)

        return self.response({'user.id': user.id})