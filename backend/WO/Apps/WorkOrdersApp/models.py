#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Status(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return '%s - %s' % (self.code, self.description)


class Person(models.Model):
    TYPES = (
         (1, 'Coordinator'),
         (2, 'Vendor'),
         (3, 'Employe'),
         (4, 'Client')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPES)
    status = models.ForeignKey(Status)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return '%s - %s' % (self.first_name, self.last_name)


class Remark(models.Model):
    description = models.TextField()
    status = models.ForeignKey(Status)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Remark'
        verbose_name_plural = 'Remarks'

    def __str__(self):
        return '%s' % (self.description)


class Order(models.Model):
    number = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    coordinator = models.ForeignKey(Person,related_name='coordinator')
    vendor = models.ForeignKey(Person,related_name='vendor')
    vendor_sub_out = models.DecimalField(max_digits=10,decimal_places=2)
    sub_out = models.DecimalField(max_digits=10,decimal_places=2)
    client = models.ForeignKey(Person,related_name='client')
    client_contract = models.CharField(max_length=20)
    status = models.ForeignKey(Status)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return '%s' % (self.number)

