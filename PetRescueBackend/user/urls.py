from django.urls import path, include

from PetRescueBackend.user.api.rest.user_api import UserApi
from PetRescueBackend.user.views.user_view import info

app_label = 'user'

api_patterns = [
    path('user/', UserApi.as_view()),
]

ui_patterns = [
    path(
        route='info/<str:profile_id>',
        view=info,
        name='profile-info'
    ),
]

urlpatterns = [
    path('', include(api_patterns)),
    path('ui/', include(ui_patterns)),
]
