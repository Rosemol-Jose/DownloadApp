# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AndroidAppViewSet, UserViewSet, AppDownloadViewSet, UserLoginView, UserSignupView

router = DefaultRouter()
router.register(r'android-apps', AndroidAppViewSet, basename='androidapp')
router.register(r'users', UserViewSet, basename='user')
router.register(r'app-downloads', AppDownloadViewSet, basename='appdownload')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]