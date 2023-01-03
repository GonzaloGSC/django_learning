from unittest import TestCase
# from unittest.mock import MagicMock, patch
from rest_framework import status
import responses, requests

class test_teams_crud(TestCase):
    @responses.activate
    def test_create_team(self):
        responses.get(
            url="http://localhost:8000/matches/team",
            json={
                'success': True,
                'error': False,
                'status_code': status.HTTP_200_OK,
                'message': "Consulta realizada con éxito.",
                'data': []
            },
            status=status.HTTP_200_OK,
        )
        response_get = requests.get("http://localhost:8000/matches/team", {"team_name": "Chile"})
        self.assertEqual({
                'success': True,
                'error': False,
                'status_code': status.HTTP_200_OK,
                'message': "Consulta realizada con éxito.",
                'data': []
            }, 
            response_get.json()
        )
        self.assertEqual(200, response_get.status_code)


# @responses.activate
# def test_create_team():
#     responses.get(
#         url="http://localhost:8000/matches/team",
#         json={
#             'success': True,
#             'error': False,
#             'status_code': status.HTTP_200_OK,
#             'message': "Consulta realizada con éxito.",
#             'data': []
#         },
#         status=status.HTTP_200_OK,
#     )
#     responses.post(
#         url="http://localhost:8000/matches/team",
#         json={
#             'success': True,
#             'error': False,
#             'status_code': status.HTTP_201_CREATED,
#             'message': "Objeto creado con éxito.",
#             'data': {}
#         },
#         status=status.HTTP_201_CREATED,
#     )
#     responses.patch(
#         url="http://localhost:8000/matches/team",
#         json={
#             'success': True,
#             'error': False,
#             'status_code': status.HTTP_200_OK,
#             'message': "Objeto modificado con éxito.",
#             'data': {}
#         },
#         status=status.HTTP_200_OK,
#     )
#     responses.delete(
#         url="http://localhost:8000/matches/team",
#         json={
#             'success': True,
#             'error': False,
#             'status_code': status.HTTP_200_OK,
#             'message': "Objeto eliminado con éxito.",
#             'data': {}
#         },
#         status=status.HTTP_200_OK,
#     )
#     resp_post = requests.post("http://localhost:8000/matches/team", json={
#         "team_name": "Chile",
#         "coach": "Gonzalo",
#         "captain": "Pelé",
#         "stadium": "",
#         "location": "Santiago, Chile",
#         "wins": 0,
#         "losses": 0,
#         "draws": 0,
#     })
#     resp_get = requests.get("http://localhost:8000/matches/team", {"team_name": "Chile"})
#     resp_patch = requests.patch("http://localhost:8000/matches/team", json={
#         "team_name": "Chile",
#         "coach": "Gonzalo",
#         "captain": "Pelé",
#         "stadium": "",
#         "location": "Santiago, Chile",
#         "wins": 0,
#         "losses": 0,
#         "draws": 0,
#     })
#     resp_delete = requests.delete("http://localhost:8000/matches/team")
#     print("resp_get.json():", resp_get.json())
#     assert resp_get.json() == {
#         'success': True,
#         'error': False,
#         'status_code': status.HTTP_200_OK,
#         'message': "Consulta realizada con éxito.",
#         'data': [""]
#     }
    # assert resp_post.json() == {"type": "post"}
    # assert resp_patch.json() == {"type": "patch"}
    # assert resp_delete.json() == {"type": "patch"}

# test_create_team()



# https://platzi.com/blog/tests-python-usando-mock/
# https://nationalize.io/#responses
# https://github.com/getsentry/responses