from accounts.models import Accounts
from .serializer import AccountSerializer

from rest_framework import viewsets


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer