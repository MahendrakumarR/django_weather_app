from django.db import models

class City(models.Model):
    name=models.CharField(max_length=25,default="")    # here 'name' is object

    def __str__(self):                                # 'name' is object so convert into string using this function
        return self.name
# Create your models here.
