from django.urls import path
from .views import (
    home,
    friend_list, 
    invites_recieved_view,
    send_friend_request,
    remove_from_friend,
    accept_friend_request,
    decline_friend_request
    # search_user
    )

urlpatterns = [
    path('', home, name='home'),
    path('friends/', friend_list, name='friend'),
    path('friendrequest/', invites_recieved_view, name='frrequest'),
    path('sendfriendrequest/', send_friend_request, name='sendfrrequest'),
    path('removefromfriend/', remove_from_friend, name='removefromfriend'),
    path('acceptfriendrequest/', accept_friend_request, name='acceptfrrequest'),
    path('declinefriendrequest/', decline_friend_request, name='declinefrrequest'),
    # path('searchusername/', search_user, name='searchafriend')
]
