from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
# from django.http import HttpResponse

class Orders():
    @staticmethod
    @api_view(['GET'])
    def listOrders(request):
        return Response({'message': 'list of orders'}, status=status.HTTP_200_OK)

class BookView(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "All books"}, status=status.HTTP_200_OK)

    def create(self, request):
        return Response({"message": "Creating a book"}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message": "Updating a book"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response({"message": "Displaying a book"}, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        return Response({"message": "Partially updating a book"}, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        return Response({"message": "Deleting a book"}, status=status.HTTP_200_OK)
