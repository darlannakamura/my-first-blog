from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from api.views import PostList, PostDetail
from api.viewsets import PostViewSet
router = routers.DefaultRouter()
router.register('postviewset', PostViewSet, 'posts')
app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
    url(r'posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
]