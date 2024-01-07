from django.urls import include, path
from .views import *
from rest_framework import routers


urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('reg', RegisterUser.as_view(), name='registration'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('api/v1/userlist/', UserListAPIList.as_view()),
    path('api/v1/userlist/<int:pk>/', UserListAPIUpdate.as_view()),
    path('api/v1/userlistdelete/<int:pk>/', UserListAPIDestroy.as_view()),
]
