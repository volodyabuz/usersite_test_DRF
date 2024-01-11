from django.urls import include, path, re_path
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('reg/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/userlist/', UserListAPIList.as_view()),
    path('api/v1/userlist/<int:pk>/', UserListAPIUpdate.as_view()),
    path('api/v1/userlistdelete/<int:pk>/', UserListAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
