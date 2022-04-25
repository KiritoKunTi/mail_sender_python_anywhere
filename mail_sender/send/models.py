from operator import mod
from django.db import models

# Create your models here.
class Info(models.Model):
    receiver_name = models.CharField('Receiver Name', max_length=30)
    subject = models.CharField('Subject', max_length=50)
    receiver_email = models.EmailField()
    message = models.TextField()
    file = models.FileField(null=True)
    
    class Meta:
        verbose_name_plural = 'Info'
        
    def __str__(self) -> str:
        return self.receiver_name