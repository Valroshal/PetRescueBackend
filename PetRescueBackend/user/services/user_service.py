import logging

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q

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

    def get_by_email(
            self,
            email: str,
            password: str,
    ) -> [UserJson, None]:
        try:
            if not email:
                raise ValidationError('profile_id is empty')

            user = self.get(
                filters=Q(Q(email=email) & Q(password=password)),
            )

            return user

        except ObjectDoesNotExist:
            return None
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex
