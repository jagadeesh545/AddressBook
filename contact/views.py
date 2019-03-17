# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from contact.models import Contact

# Create your views here.
#@login_required
class ContactList(generic.ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
