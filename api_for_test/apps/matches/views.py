from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import views

from apps.matches.services import (
    get_team,
    create_team,
    delete_team,
    update_team,
)

class v_team(APIView):
    authentication_classes = [AllowAny]
    def post(self, request, *args, **kwards):
        return create_team(request)
    def get(self, request, *args, **kwards):
        return get_team(request)
    def put(self, request, *args, **kwards):
        return update_team(request)
    def delete(self, request, *args, **kwards):
        return delete_team(request)

