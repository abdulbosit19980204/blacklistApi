from rest_framework.response import Response
from .models import *
from .serializers import  *
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from lookup.models import TelegramUser
from lookup.serializers import TelegramUserSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


# USERS
class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'surname', 'username']
    search_fields = ['name', 'surname', 'username']

# PHONES
class PhonesViewSet(ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['number', 'user']
    search_fields = ['number']

# CARDS
class CardsViewSet(ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['number', 'user']
    search_fields = ['number']

# TELEGRAM USERS
class TelegramUserViewSet(ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['telegram_id', 'username']
    search_fields = ['telegram_id', 'phone', 'username']

# FRIENDS
class FriendsView(ListAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['user', 'fullname']
    search_fields = ['fullname']

class FriendsCreate(ListCreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

class FriendsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer


class SearchApiView(APIView):
    def get(self, request):
        search_text = request.GET.get("search_text", "")

        if not search_text:
            return Response({"error": "search_text parameter is required."}, status=400)

        users = Users.objects.filter(
            Q(name__icontains=search_text) |
            Q(surname__icontains=search_text) |
            Q(username__icontains=search_text)
        )

        phones = Phones.objects.filter(
            Q(number__icontains=search_text)
        )

        cards = Cards.objects.filter(
            Q(number__icontains=search_text) |
            Q(bank__icontains=search_text)
        )

        telegram_users = TelegramUser.objects.filter(
            Q(telegram_id__icontains=search_text) |
            Q(_phone__icontains=search_text) |
            Q(username__icontains=search_text)
        )

        users_data = UsersSerializer(users, many=True).data
        phones_data = PhonesSerializer(phones, many=True).data
        cards_data = CardsSerializer(cards, many=True).data
        telegram_users_data = TelegramUserSerializer(telegram_users, many=True).data

        combined_data = {
            "users": users_data,
            "phones": phones_data,
            "cards": cards_data,
            "telegram_users": telegram_users_data
        }

        return Response(combined_data)