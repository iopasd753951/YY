from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from yea_yac import exception
from . import models


class SearchView(View):
    def get(self, request):
        query = request.GET.get['query']
        tag = request.GET.get['tag']

        if tag != 0:
            if models.Store.objects.filter(Q(store_name__contains=query) | Q(store_content__contains=query)):
                filter_data = models.Store.objects.filter(Q(store_name__contains=query) | Q(store_content__contains=query))

                return JsonResponse(list(filter_data.values()), status=200, safe=False)
            else:
                return exception.NotValueExists()
        else:
            if models.Store.objects.filter(Q(store_name__contains=query) | Q(store_content__contains=query) | Q(store_tag=tag)):
                filter_data = models.Store.objects.filter(Q(store_name__contains=query) | Q(store_content__contains=query) | Q(store_tag=tag))

                return JsonResponse(list(filter_data.values()), status=200, safe=False)
            else:
                return exception.NotValueExists()

