from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Person
from api.serializers import PersonSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def person(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        person = Person.objects.get(pk=id)
