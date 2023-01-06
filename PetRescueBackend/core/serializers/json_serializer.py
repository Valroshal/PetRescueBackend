import inspect
from dataclasses import dataclass, asdict

from PetRescueBackend.core.models import BaseModel


@dataclass
class BaseJsonSerializer:
    id: str

    @classmethod
    def from_model(
            cls,
            model: type(BaseModel)
    ):
        return cls(**{
            k: v for k, v in model.__dict__.items()
            if k in inspect.signature(cls).parameters
        })

    @classmethod
    def from_models_to_representation(
            cls,
            models: [type(BaseModel)]
    ):
        models_json = []
        for model in models:
            models_json.append(
                cls(**{
                    k: v for k, v in model.__dict__.items()
                    if k in inspect.signature(cls).parameters
                }).__dict__
            )
        return models_json

    def to_representation(self):
        return asdict(self)
