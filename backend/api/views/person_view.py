from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Person
from api.serializers import PersonSerializer


@api_view(['GET'])
def person(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        person = Person.objects.filter(pk=id)
        serializer = PersonSerializer(person, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
