from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=30)
    email = models.EmailField()
    dob = models.DateField()
    nick_name = models.CharField(max_length=40)



    def __str__(self):
        return self.first_name


    