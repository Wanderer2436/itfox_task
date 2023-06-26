from rest_framework import serializers
import core.models


class Comments(serializers.ModelSerializer):
    class Meta:
        model = core.models.Comments
        fields = '__all__'


class News(serializers.ModelSerializer):
    class Meta:
        model = core.models.News
        fields = '__all__'
