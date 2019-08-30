from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Rating, Profile, Movie

from django.contrib.auth.forms import UserCreationForm


@api_view(['POST'])
def signup(request):

    if request.method == 'POST':
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        age = request.data.get('age', None)
        occupation = request.data.get('occupation', None)
        gender = request.data.get('gender', None)

        if (username and password) :
            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)

        return Response(status=status.HTTP_201_CREATED)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
