from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.HyperlinkedRelatedField(
    #     view_name='post_detail',
    #     many=True,
    #     read_only=True
    # )
    # posts = PostSerializer()

    class Meta:
        depth = 1
        model = User
        fields = ('id', 'firstName', 'lastName', 'userId',
                  'email', 'password', 'photo_url', 'posts')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )
    user = UserSerializer()
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        depth = 1
        model = Post
        fields = ('id', 'user', 'content',
                  'created_at', 'updated_at', 'user_id')
