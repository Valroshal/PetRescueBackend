from typing import Union

from django.db.models import Q, QuerySet
from rest_framework.exceptions import ValidationError

from PetRescueBackend.core.models import BaseModel


class BaseManager(object):

    def __init__(
            self,
            model: type(BaseModel)
    ):
        try:
            self.model: type(BaseModel) = model
        except Exception as ex:
            raise ex

    @staticmethod
    def __clear_cache(
            model: type(BaseModel)
    ):
        try:
            model.save()
        except Exception as ex:
            raise ex

    def get_by_id(
            self,
            model_id,
    ) -> Union[type(BaseModel), None]:
        try:
            if not model_id:
                raise ValidationError('model_id are empty')

            result = self.model.objects.filter(pk=model_id).last()

            if not result:
                return None

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get(
            self,
            filters: Q,
            include_deleted: bool = False
    ) -> QuerySet[type(BaseModel)]:
        try:
            if not filters:
                raise ValidationError('filters empty')
            if not include_deleted:
                filters = Q(filters, is_deleted=False)

            result = self.model.objects.filter(filters)

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_related(
            self,
            filters: Q,
            related_params: str,
            include_deleted: bool = False
    ) -> QuerySet[type(BaseModel)]:
        try:
            if not filters:
                raise ValidationError('filters empty')
            if not related_params:
                raise ValidationError('related_params empty')
            if not include_deleted:
                filters = Q(filters, is_deleted=False)

            result = self.model.objects.filter(filters).select_related(related_params)

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_value_list(
            self,
            filters: Q,
            value: str,
            include_deleted: bool = False
    ) -> QuerySet:
        try:
            if not filters:
                raise ValidationError('filters empty')
            if not value:
                raise ValidationError('value empty')
            if not include_deleted:
                filters = Q(filters, is_deleted=False)

            result = self.model.objects.filter(filters).values_list(value, flat=True)

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_values_list(
            self,
            filters: Q,
            values: [str],
            include_deleted: bool = False
    ) -> QuerySet:
        try:
            if not filters:
                raise ValidationError('filters empty')
            if not values:
                raise ValidationError('values empty')
            if not include_deleted:
                filters = Q(filters, is_deleted=False)

            result = self.model.objects.filter(filters).values_list(*values)

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_or_create(
            self,
            **kwargs
    ) -> type(BaseModel):
        try:

            if not kwargs:
                raise ValidationError('kwargs empty')

            model, is_created = self.model.objects.get_or_create(**kwargs)

            return model

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def create(
            self,
            **kwargs
    ) -> type(BaseModel):
        try:
            if not kwargs:
                raise ValidationError('kwargs empty')

            model = self.model.objects.create(**kwargs)

            return model

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def bulk_create(
            self,
            objs: [any]
    ) -> type(BaseModel):
        try:
            if not objs:
                raise ValidationError('objs empty')

            objs = [self.model(**vals) for vals in objs]

            models = self.model.objects.bulk_create(objs)

            if models:
                self.__clear_cache(model=models[0])

            return models

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def bulk_update(
            self,
            objs: [any]
    ) -> type(BaseModel):
        try:
            if not objs:
                raise ValidationError('objs empty')

            objs = [self.model(**vals) for vals in objs]

            models = self.model.objects.bulk_update(objs)

            if models:
                self.__clear_cache(model=models[0])

            return models

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def update(
            self,
            model_id: any,
            **kwargs
    ) -> type(BaseModel):
        try:
            if not model_id:
                raise ValidationError('model_id empty')
            if not kwargs:
                raise ValidationError('kwargs empty')

            self.model.objects.filter(pk=model_id).update(**kwargs)
            model = self.model.objects.filter(pk=model_id).last()

            if model:
                self.__clear_cache(model=model)

            return model

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def is_exist(
            self,
            model_id: str,
    ) -> bool:
        try:
            if not model_id:
                raise ValidationError('model_id empty')

            result = self.model.objects.filter(pk=model_id).exists()

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def delete(
            self,
            model_id: any,
    ):
        try:
            if not model_id:
                raise ValidationError('model_id empty')

            delete_obj = self.model.objects.filter(pk=model_id).last()
            delete_obj.is_deleted = True
            delete_obj.save()

            if delete_obj:
                self.__clear_cache(model=delete_obj)

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def hard_delete(
            self,
            model_id: any,
    ) -> type(BaseModel):
        try:
            if not model_id:
                raise ValidationError('model_id empty')

            delete_obj = self.model.objects.filter(pk=model_id).last()

            if delete_obj:
                self.__clear_cache(model=delete_obj)

            delete_obj.delete()

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex
