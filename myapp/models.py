from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=60, blank=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.nome