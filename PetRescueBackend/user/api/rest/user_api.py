from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from rest_framework.response import Response

from PetRescueBackend.user.serializers.user_json import UserJson
from PetRescueBackend.user.services.user_service import UserService


class UserApi(APIView):

    def post(self, request):
        try:

            user_json = UserService().create(
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                email=request.data['email'],
                password=request.data['password']
            )

            return Response(
                data=user_json.to_representation(),
                status=status.HTTP_200_OK
            )

        except ValidationError as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request):
        try:

            user = UserService().get_by_email(
                email=request.data['email'],
                password=request.data['password'],
            )

            return Response(
                data=user.to_representation(),
                status=status.HTTP_200_OK
            )

        except ObjectDoesNotExist:
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
