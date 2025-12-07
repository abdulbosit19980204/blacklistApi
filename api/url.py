from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, PhonesViewSet, CardsViewSet, TelegramUserViewSet, FriendsView, FriendsCreate, FriendsUpdate, SearchApiView

router = DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('phones', PhonesViewSet, basename='phones')
router.register('cards', CardsViewSet, basename='cards')
router.register('telegram-users', TelegramUserViewSet, basename='telegram-users')

urlpatterns = router.urls

urlpatterns += [
    path('friends/', FriendsView.as_view(), name='friends-list'),
    path('friends/post/', FriendsCreate.as_view(), name='friends-create'),
    path('friends/<int:pk>/', FriendsUpdate.as_view(), name='friends-update'),
    path('search/', SearchApiView.as_view(), name='search-api'),
]