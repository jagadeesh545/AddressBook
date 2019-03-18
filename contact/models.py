# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Contact(models.Model):
    """Model to store contact details in the database. Main model for AddressBook project"""
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.PositiveIntegerField()
    email_address = models.EmailField()
    street_address = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


    class Meta:
        db_table = "contact"
