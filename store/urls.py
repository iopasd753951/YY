from django.urls import path, include

from . import views

urlpatterns = [
    path('v1/search', views.SearchView.as_view(), name="v1_store_search"),
]
