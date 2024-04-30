from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'classes', views.ClassRoomViewSet)
router.register(r'assessments', views.AssessmentViewSet)
router.register(r'questions', views.QuestionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls'), name="rest_framework"),
]
