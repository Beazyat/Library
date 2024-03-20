from django.shortcuts import render
from django.views.generic import ListView, DetailView

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics

from .models import *
from .serializers import BookSerializers


# def index(request):
#     num_book = Book.objects.all().count()
#     num_author = Author.objects.count()
#     num_book_available = BookInstance.objects.filter(status__exact="a").count()
    
#     context = {
#         "num_book" : num_book,
#         "num_author" : num_author,
#         "num_book_available" : num_book_available,
#     }
#     return render(request, "book/index.html", context)


class BookListView(ListView):
    model = Book
    template_name = "book/index.html"
    context_object_name = "book_list"
    extra_context = {'authors': Author.objects.all()}
    paginate_by = 5


class BookDeatail(DetailView):
    model = Book
    template_name = "book/detail.html"
    context_object_name = 'book'



# class APIListBook(APIView):
#     def get(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializers(books, many=True)
        
#         return Response(serializer.data)
        
#     def post(self, request, format=None):
#         serializers = BookSerializers(data = request.data)
#         serializers.is_valid(raise_exception = True)
#         serializers.save()
#         return Response(serializers.data, status = status.HTTP_201_CREATED) 
"""
All of that codes using for made api and use that for get and save post in database wtih functional programing! 
"""


class ListCreateCource(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class RetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers