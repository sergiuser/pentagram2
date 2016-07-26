from django.contrib.auth.models import User
from pentagram.models import Photo, Comment
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id', 'username', 'password','email')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Photo
        fields = ('id', 'user', 'counter_like', 'photo')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'photo', 'comment')