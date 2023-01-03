from requests import request, Request
from rest_framework.response import Response
from rest_framework import status

from apps.log_sys.services import manage_and_respond_exceptions, create_logger
from apps.matches.models import (
    m_match,
    m_team,
)
from apps.matches.serializers import (
    s_match,
    s_team,
)

LOGGER = create_logger("matches.log")

def create_team(request: Request):
    try:
        serializer = s_team(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {
            'success': True,
            'error': False,
            'status_code': status.HTTP_201_CREATED,
            'message': "Objeto creado con éxito.",
            'data': {}
        }
        return Response(data=response_data, status=response_data["status_code"], content_type="application/json")
    except Exception as err:
        return manage_and_respond_exceptions(err, LOGGER)


def update_team(request: Request):
    try:
        team = m_team.objects.filter(team_name=request.data["team_name"]).first()
        if team:
            serializer = s_team(data=request.data, instance=team)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                'success': True,
                'error': False,
                'status_code': status.HTTP_200_OK,
                'message': "Objeto modificado con éxito.",
                'data': {}
            }
        else:
            response_data = {
                'success': False,
                'error': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Equipo no encontrado en registros, modificación cancelada.",
                'data': {}
            }
        return Response(data=response_data, status=response_data["status_code"], content_type="application/json")
    except Exception as err:
        return manage_and_respond_exceptions(err, LOGGER)


def get_team(request: Request):
    try:
        teams = m_team.objects.filter(**request.GET)
        serializer = s_team(teams, many=True)
        teams_list = list(serializer.data)
        response_data = {
            'success': True,
            'error': False,
            'status_code': status.HTTP_200_OK,
            'message': "Consulta realizada con éxito.",
            'data': teams_list
        }
        return Response(data=response_data, status=response_data["status_code"], content_type="application/json")
    except Exception as err:
        return manage_and_respond_exceptions(err, LOGGER)


def delete_team(request: Request):
    try:
        team = m_team.objects.filter(team_name=request.data["team_name"]).first()
        if team:
            team.delete()
            response_data = {
                'success': True,
                'error': False,
                'status_code': status.HTTP_200_OK,
                'message': "Objeto eliminado con éxito.",
                'data': {}
            }
        else:
            response_data = {
                'success': False,
                'error': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': "Equipo no encontrado en registros, eliminación cancelada.",
                'data': {}
            }
        return Response(data=response_data, status=response_data["status_code"], content_type="application/json")
    except Exception as err:
        return manage_and_respond_exceptions(err, LOGGER)