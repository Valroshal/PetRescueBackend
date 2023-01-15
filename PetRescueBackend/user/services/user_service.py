import logging

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse

from PetRescueBackend.core.models import BaseModel
from PetRescueBackend.core.services.base_manager import BaseManager
from PetRescueBackend.user.models import User
from PetRescueBackend.user.serializers.user_json import UserJson

logger = logging.getLogger(__name__)


class UserService(BaseManager):
    def __init__(self):
        try:
            super().__init__(model=User)
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex

    def get_by_id(
            self,
            user_id,
    ) -> [UserJson, None]:
        try:
            user = super().get_by_id(model_id=user_id)

            if not user:
                raise ObjectDoesNotExist

            user_json = UserJson.from_model(user)

            return user_json

        except ObjectDoesNotExist:
            return None
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex

    def get_by_email(
            self,
            email: str,
            password: str,
    ) -> [UserJson, None]:
        try:
            if email is None:
                raise ValidationError('email is empty')

            if password is None:
                raise ValidationError('password is empty')

            # TODO here user is empty, can't understand what's the problem
            # user = self.get(
            #     filters=Q(Q(email=email) & Q(password=password)),
            # ).all()

            user = User.objects.get(email=email, password=password)

            if not user:
                raise ValidationError('user does not exist')

            return UserJson.from_model(user)

        except ObjectDoesNotExist:
            return None
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex

    @transaction.atomic
    def create(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str
    ):
        try:
            # check if not exist
            user_exist = self.get_by_email(
                email=email,
                password=password
            )

            if user_exist:
                raise ValidationError('user already exists')

            # create user
            user = super().create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

            user_json = UserJson.from_model(user)

            return user_json

        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex
