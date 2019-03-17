# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ContactList(generic.ListView):
    model = Contact
    template_name = 'contact/contact_list.html'

    def dispatch(self, *args, **kwargs):
        return super(generic.ListView, self).dispatch(*args, **kwargs)
