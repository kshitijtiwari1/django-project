from django.db import models

# Create your models here.
class model_a(models.Model):
    field1 = models.CharField(max_length=50, blank = True, null = True)