from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('reg', RegisterUser.as_view(), name='registration'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('api/v1/userlist', UserListAPIView.as_view())
]
