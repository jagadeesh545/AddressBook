# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ContactList(generic.ListView):
    model = Contact
    paginate_by = 20
    template_name = 'contact/contact_list.html'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def dispatch(self, *args, **kwargs):
        return super(generic.ListView, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class AddContact(generic.CreateView):
    model = Contact
    fields = [
        'first_name',
        'last_name',
        'phone_number',
        'email_address',
        'street_address',
    ]
    template_name = 'contact/add_contact.html'
    success_url = reverse_lazy('contact_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(generic.CreateView, self).form_valid(form)

    def dispatch(self, *args, **kwargs):
        return super(generic.CreateView, self).dispatch(*args, **kwargs)
