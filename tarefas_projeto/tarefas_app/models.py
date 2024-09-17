from django.db import models
from django.utils import timezone

class SoftDeleteModel(models.Model):

    is_active = models.BooleanField(editable = False, default=True)
    created_at = models.DateTimeField( auto_now_add =True)
    updated_at = models.DateTimeField( auto_now=True)
    deleted_at = models.DateTimeField( editable=False,blank=True, null=True)

    def delete(self, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
    def hard_delete (self, **kwargs):
        super(SoftDeleteModel, self).delete(**kwargs)

    class Meta:
        abstract = True

class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=timezone.now() ,is_active=False)

class BaseManager(models.Manager):
    def get_queryset (self):
        return BaseModelQuerySet( self.model, using=self._db).filter( deleted_at__isnull =True, is_active=True)
    

class Category(SoftDeleteModel):
    name = models.CharField(max_length=100)

    objects = BaseManager()

    def __str__(self):
        return self.name


class Priority(SoftDeleteModel):
    level = models.CharField(max_length=50)

    objects = BaseManager()

    def __str__(self):
        return self.level


class Task(SoftDeleteModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, related_name='tasks', on_delete=models.CASCADE)

    objects = BaseManager()

    def __str__(self):
        return self.title
