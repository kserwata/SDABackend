from django.db import models, DEFAULT_DB_ALIAS


class DeletableQueryManager(models.Manager):
    def get_queryset(self):
        return super(DeletableQueryManager, self).get_queryset().filter(is_deleted=False)


class DeletableModel(models.Model):

    is_deleted = models.BooleanField(default=False)

    objects = DeletableQueryManager()
    default_manager = models.Manager()

    def delete(self, using=DEFAULT_DB_ALIAS, keep_parents=False):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
