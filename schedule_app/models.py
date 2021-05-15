from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Chief(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'chief'
        verbose_name = 'chief'
        verbose_name_plural = 'chiefs'


class Worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    chief = models.ManyToManyField(Chief)

    class Meta:
        db_table = 'worker'
        verbose_name = 'worker'
        verbose_name_plural = 'workers'


class Schedule(models.Model):
    name = models.CharField(max_length=256)
    workers = models.ManyToManyField(Worker)

    class Meta:
        db_table = 'schedule'
        verbose_name = 'schedule'
        verbose_name_plural = 'schedules'


class Task(models.Model):
    title = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'task'

