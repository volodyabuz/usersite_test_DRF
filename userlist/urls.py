from django.urls import include, path
from .views import *
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
    ]

router = MyCustomRouter()
router.register(r'userlist', UserListViewSet)
print(router.urls)

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('reg', RegisterUser.as_view(), name='registration'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/userlist/', UserListViewSet.as_view({'get': 'list'})),
    # path('api/v1/userlist/<int:pk>/', UserListViewSet.as_view({'put': 'update'})),
]
