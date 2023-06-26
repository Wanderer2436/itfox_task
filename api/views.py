from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api import serializers, pagination, datatools
import core.models


class NewsViewSet(ModelViewSet):
    queryset = core.models.News
    serializer_class = serializers.News
    pagination_class = pagination.CustomPagination

    @action(detail=True, methods=['post'], serializer_class=None)
    def add_or_remove_like(self, request: Request, pk: int) -> Response:
        datatools.news.add_or_remove_like(news=self.get_object(), user=self.request.user)
        return Response({'Response': 'OK'})


class CommentsViewSet(ModelViewSet):
    queryset = core.models.Comments
    serializer_class = serializers.Comments
    pagination_class = pagination.CustomPagination
