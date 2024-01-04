from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'userlist', UserListViewSet)

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('reg', RegisterUser.as_view(), name='registration'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/userlist/', UserListViewSet.as_view({'get': 'list'})),
    # path('api/v1/userlist/<int:pk>/', UserListViewSet.as_view({'put': 'update'})),
]
