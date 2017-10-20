from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^index/', include(router.urls), name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
