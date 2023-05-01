from django.db import models
from django.utils import timezone

# Create your models here.

class Koan(models.Model):

    ACTIVE = 1
    INACTIVE = 0

    STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    koan = models.TextField(max_length=16777215)
    status = models.IntegerField(
        choices=STATUS,
        default=1
    )
    created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField()
    # deleted_at = models.DateTimeField(default=None, null=True)
