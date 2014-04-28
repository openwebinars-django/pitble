from django.db import models
from django.db.models.query import QuerySet


class PitbleQuerySet(QuerySet):

    def by_owner(self, owner):
        return self.filter(owner=owner)


class PitbleManager(models.Manager):

    def get_query_set(self):
        return PitbleQuerySet(self.model, using=self._db)

    def by_owner(self, owner):
        return self.get_query_set().by_owner(owner)