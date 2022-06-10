from django.db import models

# Create your models here.
class Recipient(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.email