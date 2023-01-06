from dataclasses import dataclass

from PetRescueBackend.core.serializers.json_serializer import BaseJsonSerializer


@dataclass
class UserJson(BaseJsonSerializer):
    name: str
    email: str
    phone: str = None
    user_id: str = None
