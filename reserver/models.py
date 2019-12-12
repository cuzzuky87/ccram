import uuid
from django.db import models

from accounts.models import User


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    start_at=models.DateTimeField(auto_now=False)
    end_at = models.DateTimeField(auto_now=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='予約者')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title