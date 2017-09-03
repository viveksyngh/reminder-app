from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate 

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer, PasswordSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing and editing user instances
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def parsed_query_data(self, request):
        data = {}
        for key, value in request.data.items():
            data[key]=value
        return data

    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=self.parsed_query_data(request))
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error": "Login Failed"}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

