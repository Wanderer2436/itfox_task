from rest_framework import serializers
import core.models


class CommentsRead(serializers.ModelSerializer):
    class Meta:
        model = core.models.Comments
        fields = '__all__'


class CommentsWrite(serializers.ModelSerializer):
    class Meta:
        model = core.models.Comments
        fields = ('news', 'text',)


class NewsRead(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    last_comments = serializers.SerializerMethodField()

    class Meta:
        model = core.models.News
        fields = '__all__'

    def get_comments_count(self, obj: core.models.News):
        return obj.comments.count()

    def get_last_comments(self, obj: core.models.News):
        comments = obj.comments.all()[:10]
        return CommentsRead(comments, many=True).data


class NewsWrite(serializers.ModelSerializer):
    class Meta:
        model = core.models.News
        fields = ('title', 'text',)
