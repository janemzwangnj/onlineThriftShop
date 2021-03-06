from rest_framework import generics
from .serializers import UserSerializer, ItemSerializer, ShopcardSerializer
from .models import User, Item, Shopcard


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    # lookup_url_kwarg = 'email'
    lookup_field = 'email'

    def get_queryset(self):
        return User.objects.filter()


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ShopcardList(generics.ListCreateAPIView):
    queryset = Shopcard.objects.all()
    serializer_class = ShopcardSerializer


class ShopcardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shopcard.objects.all()
    serializer_class = ShopcardSerializer
