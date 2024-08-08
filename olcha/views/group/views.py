from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from olcha.models import GroupModel
from olcha.serializers import GroupModelSerializer


class GroupCreateApiView(generics.CreateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer


class GroupListAPIView(generics.ListCreateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer
    lookup_field = 'slug'


# class GroupListAPIView(APIView):
#     def get(self, request):
#         groups = GroupModel.objects.all()
#         serializer = GroupModelSerializer(groups, many=True, context={'request': request})
#         return Response(serializer.data, status=HTTP_200_OK)


class GroupDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer
    lookup_field = 'slug'


