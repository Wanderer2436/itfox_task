from rest_framework.viewsets import ModelViewSet

from api import serializers, pagination
import core.models


class NewsViewSet(ModelViewSet):
    queryset = core.models.News
    serializer_class = serializers.News
    pagination_class = pagination.CustomPagination


class CommentsViewSet(ModelViewSet):
    queryset = core.models.Comments
    serializer_class = serializers.Comments
    pagination_class = pagination.CustomPagination
