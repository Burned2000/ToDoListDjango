from django.db import models

# Create your models here.
class ToDo(models.Model):
    to_do_text=models.CharField(max_length=255,null=True,blank=True)
    created=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.to_do_text)
    
    