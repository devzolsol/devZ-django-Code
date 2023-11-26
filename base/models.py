import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):

    STATUS_CHOICES = (('Not Contacted', 'Not Contacted'),
                     ('Initiated', 'Initiated'),
                     ('Pending', 'Pending'),
                     ('Accepted', 'Accepted'),
                     ('Rejected', 'Rejected'))

    client_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=50000, null=True, blank=True)
    l_name = models.CharField(max_length=50000, null=True, blank=True)
    company_name = models.CharField(max_length=50000, null=True, blank=True)
    address = models.CharField(max_length=50000, null=True, blank=True)
    address_phone = models.CharField(max_length=50000, null=True, blank=True)
    phone = models.CharField(max_length=50000, null=True, blank=True)
    email = models.CharField(max_length=50000, null=True, blank=True)
    is_mailed = models.BooleanField(default=False)
    last_mail_date = models.DateField(auto_now=True, null=True, blank=True)
    count = models.IntegerField(default=0)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Not Contacted')
    note = models.TextField(null=True, blank=True)

    last_edited = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.company_name}"

