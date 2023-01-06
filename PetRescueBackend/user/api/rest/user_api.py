from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from PetRescueBackend.user.services.user_service import UserService


class UserApi(APIView):

    def get(self, request):
        try:
            user_json = UserService().get_by_email(
                email=request.email,
                password=request.password,
            )

            if not user_json:
                raise ObjectDoesNotExist

            return Response(
                data=user_json.to_representation(),
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
