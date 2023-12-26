from django.db import models


class UserList(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    dob = models.DateField(blank=True, verbose_name='Дата рождения')
    sex_id = models.ForeignKey('MaleFemale',on_delete=models.CASCADE, default=1, verbose_name='Пол')

    def __str__(self):
        return self.first_name

class MaleFemale(models.Model):
    sex = models.CharField(max_length=1, unique=True, verbose_name='Пол')

    def __str__(self):
        return self.sex
