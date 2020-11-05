from django.shortcuts import render
from django import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Play_listSerializer, Play_listSerializerModel
# берем плеер-лист и автора, и что-то с ними делаем в методе пост


class Something(APIView):


    def post(self, request):
        serializer = Play_listSerializer(data=request.data)

        serializer.is_valid()

        instance = serializer.save()




        return Response(request.data)


# Create your views here.
