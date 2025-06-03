import os

from django.shortcuts import get_object_or_404
import json, requests
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.request import Request

from restaurant.models import Restaurant

# Create your views here.

@api_view(['GET'])
def healthcheck(request):
    return JsonResponse({"message": "restaurant service is running!"}, status=200)

@api_view(['GET'])
def get_restaurants(request, restaurant_id):
    #get the restaurant out of the db using the restaurant_id as key
    restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)

    #create the json dict
    restaurant_data = {
        'name': restaurant.name,
        'address': restaurant.address,
        'city': restaurant.city,
        'tags': restaurant.tags,
        'description': restaurant.description
    }

    return JsonResponse(restaurant_data, safe=False, status=200)

@api_view(['POST'])
def add_restaurant(request: Request) -> JsonResponse:
    #get the request body
    request_body = json.loads(request.body)

    #get the data from the request body
    r_name = request_body.get('name')
    r_city = request_body.get('city')
    r_tags = request_body.get('tags')
    r_address = request_body.get('address')
    r_description = request_body.get('description')
    r_place_id = None

    #create a new restaurant object
    restaurant = Restaurant.objects.create(
        name=r_name,
        city=r_city,
        tags=r_tags,
        address=r_address,
        description=r_description,
        place_id=r_place_id
    )

    return JsonResponse({"restaurant": restaurant.restaurant_id}, status=200)

@api_view(['DELETE'])
def delete_restaurant(request: Request, restaurant_id: str) -> HttpResponse:
    #get the restaurant from the db
    restaurant = get_object_or_404(Restaurant, restaurant_id=restaurant_id)
    restaurant_id = restaurant.restaurant_id
    restaurant_name = restaurant.name

    #delete the restaurant
    restaurant.delete()

    return HttpResponse(f"deleted restaurant {restaurant_name} with id: {restaurant_id}" ,status=200)