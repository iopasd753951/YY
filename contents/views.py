from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


class HomeView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    template_name = 'home.html'

# dispatch : 요청이 get, post 같은 정상 메소드인지 확인 후 핸들러 함수로 request, *args, **kwargs를 넘겨줌
