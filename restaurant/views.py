import os

from django.shortcuts import get_object_or_404
import json, requests
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.decorators import api_view

from restaurant.models import Restaurant

# Create your views here.

@api_view(['GET'])
def healthcheck(request):
    return JsonResponse({"message": "restaurant service is running!"}, status=200)

@api_view(['GET'])
def get_restaurants(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
    return JsonResponse({"restaurants": restaurant.name}, safe=False)

@api_view(['POST'])
def add_restaurant(request):
    restaurant = Restaurant.objects.create(name="testrestaurant", city="berlin", tags=["food, drink"])
    return JsonResponse({"restaurant": restaurant.restaurant_id}, status=201)