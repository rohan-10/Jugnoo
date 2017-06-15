from django.shortcuts import render
from .serializer import AssetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import status
from rest_framework.decorators import api_view


class AssetAdd(APIView):


    def post(self, request, format=None):
        serializer = AssetSerializer(data=request.DATA)
        print(serializer.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
