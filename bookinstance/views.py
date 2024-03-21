from django.shortcuts import render
from django.views.generic import ListView, DetailView

# for function
from django.contrib.auth.decorators import login_required  # just for def and for redirect anonymous to login page

# for generics
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# in library behet ejaze mide ke vase class base viewt ye test benevisi masalan:
# agar user fagat email in bood in dastresi ro dashte bashe va betone az kelas estefade bokone

from django.contrib.auth.mixins import PermissionRequiredMixin
# mige bayad permision dashte bashi ta betone be class view dastresi dashte bashi


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics

from .models import *
from .serializers import BookSerializers

'''
@permission_required("permission_name[in meta of model")
def index(request):
    num_book = Book.objects.all().count()
    num_author = Author.objects.count()
    num_book_available = BookInstance.objects.filter(status__exact="a").count()
    
    context = {
        "num_book" : num_book,
        "num_author" : num_author,
        "num_book_available" : num_book_available,
    }
    return render(request, "book/index.html", context)
'''


class BookListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/index.html"
    context_object_name = "book_list"
    extra_context = {'authors': Author.objects.all()}
    paginate_by = 5

    login_url = 'accounts/login'
    redirect_field_name = 'book/'

    permission_required = 'bookinstance.vip'
    # intory ta dastresi vip nadashte bashi nmitioni page ro bbini va error 403 mide
    permission_required = 'user.can_edit'
    # other permission form auth module

class BookDetail(DetailView):
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


class LoanListView(LoginRequiredMixin, ListView):
    model = BookInstance
    context_object_name = 'book_instance'
    template_name = "book/bookinsstance_list_borrow.html"
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact="b").order_by("due_back")
