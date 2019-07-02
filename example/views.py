from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404






from example.models import Example
from example.models import Example2

from example.serializer import ExampleSerializers
from example.serializer import Example2Serializers

class ExampleList(APIView):
    
    def get(self, request, format=None):
        queryset = Example.objects.filter(delete=False)
        serializer = ExampleSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ExampleSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ExampleDetail(APIView):
    def get_object(self, id):
        try:
            return Example.objects.get(pk=id, delete=False)
        except Example.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ExampleSerializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Example.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ExampleSerializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Vistas de modelo Example2

class Example2List(APIView):
    
    def get(self, request, format=None):
        queryset = Example2.objects.filter(delete=False)
        serializer = Example2Serializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Example2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class Example2Detail(APIView):
    def get_object(self, id):
        try:
            return Example2.objects.get(pk=id, delete=False)
        except Example2.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = Example2Serializers(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Example2.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = Example2Serializers(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

        

    



    


