from django.db import models

# Create your models here.
class ContactPost(models.Model):
    name=models.CharField(max_length=30,default=None)
    mail=models.EmailField(default=None)
    subj=models.CharField(max_length=12)
    msg=models.TextField(null=True)
