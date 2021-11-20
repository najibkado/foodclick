from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, EntitySerializer, ListingSerializer, GiveawaySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User, Entity, Listing, Giveaway
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "main/index.html")


class LogoutApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LoginApiView(APIView):

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')


        authenticated_user = authenticate(request, username=username, password=password)

        

        if authenticated_user is not None:

            serializer = UserSerializer(authenticated_user)
            token = Token.objects.get(user=authenticated_user).key

            return Response({ 'user_id': authenticated_user.id, 'user':serializer.data ,'token': token }, status=status.HTTP_201_CREATED)

            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserRegisterApiView(APIView):

    # def get(self, request):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user)
            return Response({'user_id': user.id, 'data': serializer.data, 'token': token.key }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntitiesApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EntitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Entity.objects.filter(user=request.user)
        serializer = EntitySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EntityApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        
        try:
            return Entity.objects.get(pk=id)
        except Entity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        entityObj = self.get_object(id)
        serializer = EntitySerializer(entityObj)
        return Response(serializer.data)

    def put(self, request, id):
        entityObj = self.get_object(id)
        serializer = EntitySerializer(entityObj ,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        entityObj = self.get_object(id)
        entityObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ListingsApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ListingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Entity.objects.filter(user=request.user)
        serializer = ListingSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListingApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        
        try:
            return Listing.objects.get(pk=id)
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        listingObj = self.get_object(id)
        serializer = ListingSerializer(listingObj)
        return Response(serializer.data)

    def put(self, request, id):
        listingObj = self.get_object(id)
        serializer = ListingSerializer(listingObj ,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        listingObj = self.get_object(id)
        listingObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GiveawaysApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = GiveawaySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Entity.objects.filter(user=request.user)
        serializer = GiveawaySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GiveawayApiView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        
        try:
            return Giveaway.objects.get(pk=id)
        except Giveaway.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        giveawayObj = self.get_object(id)
        serializer = GiveawaySerializer(giveawayObj)
        return Response(serializer.data)

    def put(self, request, id):
        giveawayObj = self.get_object(id)
        serializer = GiveawaySerializer(giveawayObj ,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        giveawayObj = self.get_object(id)
        giveawayObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


