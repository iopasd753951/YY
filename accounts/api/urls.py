from accounts.api.views import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'account', AccountViewSet, basename='accounts')
urlpatterns = router.urls

# router viewset과 함께 쓸 수 있고 자동으로 url들을 관리해줌
# 들어온 요청과 그에 view action 을 함
