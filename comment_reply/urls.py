from rest_framework.routers import DefaultRouter

from comment_reply.views import CommentReplyViewSet

router = DefaultRouter()
router.register("comments", CommentReplyViewSet)

urlpatterns = router.urls
