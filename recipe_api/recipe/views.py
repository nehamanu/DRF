from django.shortcuts import render
from rest_framework.views import APIView

from recipe import serializers
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer
from rest_framework.response import Response

# Create your views here.
class RecipeCreate(APIView):
    def post(self,request):
        qs=request.data
        serializer_instance = RecipeSerializer(data=qs)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class RecipeList(APIView):
    def get(self,request):
        qs=Recipe.objects.all()
        serializer_instance=RecipeSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

class Recipeid(APIView):
    def get(self,request,i):
        r=Recipe.objects.get(id=i)
        serializer_instance=RecipeSerializer(r)
        return Response(data=serializer_instance.data)

class RecipeFullupdate(APIView):
    def put(self,request,i):
        r = Recipe.objects.get(id=i)
        serializer_instance = RecipeSerializer(r)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class RecipePartialupdate(APIView):
    def patch(self,request,i):
        r = Recipe.objects.get(id=i)
        serializer_instance = RecipeSerializer(r)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class Recipedelete(APIView):
    def delete(self,request,i):
        r = Recipe.objects.get(id=i)
        r.delete()
        return Response({"message":"Deleted Successfully"})

