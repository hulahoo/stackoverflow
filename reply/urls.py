from rest_framework.routers import DefaultRouter

from reply.views import ReplyViewSet

router = DefaultRouter()
router.register('replies', ReplyViewSet)

urlpatterns = router.urls
