from dataclasses import dataclass

from PetRescueBackend.core.serializers.json_serializer import BaseJsonSerializer


@dataclass
class UserJson(BaseJsonSerializer):
    id: str
    first_name: str
    last_name: str
    email: str

