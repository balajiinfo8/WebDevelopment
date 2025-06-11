from django.db import models
from django.utils.timezone import now


# Create your models here.
class TODOAPP(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # age = models.IntegerField(null=False, blank=True)
    age = models.IntegerField(null=True, blank=True,default=0)
    gender = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(default=now, editable=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
