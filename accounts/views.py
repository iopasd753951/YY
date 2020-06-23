import json

from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .models import Accounts


class UserSignupView(View):
    # @method_decorator(csrf_exempt) # ajax 통신시(POST요청) CSRF 토큰요구로 에러가 발생하는데 그것을 우회함
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserSignupView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        print(data)

        if Accounts.objects.filter(email=data['email']).exists():
            return JsonResponse({'Message': '이메일이 존재합니다. 다른 이메일을 적어주세요.'},  status=400)

        if Accounts.objects.filter(name=data['name']).exists():
            return JsonResponse({'Message': '존재하는 이름입니다.'}, status=400)

        Accounts(
            email=data['email'],
            name=data['name'],
            password=data['password'],
            phone=data['phone']
        ).save()
        return HttpResponse(status=200)


class UserLoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Accounts.objects.filter(email=data['email']).exists():
                user = Accounts.objects.get(email=data['email'])

                if data['password'] == user.password:
                    return HttpResponse(200)

                return HttpResponse(401)

            return HttpResponse(400)

        except KeyError:
            return HttpResponse(400)
