from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth'),
]

router = DefaultRouter()

router.register('news', views.NewsViewSet, basename='news')
router.register('comments', views.CommentsViewSet, basename='comments')

urlpatterns += router.urls
