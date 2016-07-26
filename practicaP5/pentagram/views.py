

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from pentagram.models import Photo, Comment, Like
from pentagram.serializers import UsersSerializer, PhotoSerializer, CommentSerializer
from django.core.exceptions import ObjectDoesNotExist



@api_view(['POST'])
@permission_classes((AllowAny,))
def users(request):
    if request.method == 'POST':
        user_serializer = UsersSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=user_serializer.errors)


@api_view(['GET', 'POST'])
def photos(request):
    if request.method == 'GET':
        all_photos = Photo.objects.all()
        photo_serializer = PhotoSerializer(all_photos, many=True)
        return Response(status=status.HTTP_200_OK, data=photo_serializer.data)

    if request.method == 'POST':
        photo_serializer = PhotoSerializer(data=request.data)
        if photo_serializer.is_valid():
            photo_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=photo_serializer.errors)


@api_view(['GET', 'POST'])
def comments(request, id_photo):
    if request.method == 'GET':
        all_comments = Comment.objects.filter(photo_id=id_photo)
        comments_serializer = CommentSerializer(all_comments, many=True)
        return Response(status=status.HTTP_200_OK, data=comments_serializer.data)
    if request.method == 'POST':
        comments_serializer = CommentSerializer(data=request.data)
        if comments_serializer.is_valid():
            comments_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=comments_serializer.errors)


@api_view(['PUT'])
def like(request, id_photo):
    if request.method =="PUT":
        id_user = request.user.id
        try:
            liked_photo = Like.objects.get(photo=id_photo, user=id_user)
            liked_photo.delete()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            add_like = Like(user_id=id_user, photo_id=id_photo)
            add_like.save()
            return Response (status=status.HTTP_202_ACCEPTED)




