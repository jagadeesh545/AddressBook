# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from contact.models import Contact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, resolve
from django.conf.urls import url
from contact.forms import ContactSearchForm
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class ContactList(generic.ListView, generic.edit.FormView):
    model = Contact
    form_class = ContactSearchForm
    paginate_by = 20
    template_name = 'contact/contact_list.html'

    def form_valid(self, form):
        return super(generic.edit.FormView, self).form_valid(form)

    def get_queryset(self):
        try:
            letter_val = self.kwargs['letter']
        except:
            letter_val = ''
        print('letter value = '+letter_val)
        filter_val = self.request.GET.get('search_name', '')
        if not letter_val:
            result = Contact.objects.filter(user=self.request.user).filter(
                Q(first_name__icontains=filter_val)
                |Q(last_name__icontains=filter_val)
            ).order_by('first_name')
        elif not filter_val:
            result = Contact.objects.filter(user=self.request.user).filter(
                Q(first_name__startswith=letter_val)
                |Q(first_name__startswith=letter_val.lower())
                |Q(last_name__startswith=letter_val)
                |Q(last_name__startswith=letter_val.lower())
            ).order_by('first_name')
        else:
            result = Contact.objects.filter(
                user=self.request.user
            ).order_by('first_name')
        return result

    def get_context_data(self, **kwargs):
        context = super(ContactList, self).get_context_data(**kwargs)
        context['search_name'] = self.request.GET.get('search_name', '')
        return context

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


@method_decorator(login_required, name='dispatch')
class ViewContact(generic.DetailView):
    model = Contact
    template_name = 'contact/view_contact.html'

    def dispatch(self, *args, **kwargs):
        return super(generic.DetailView, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class DeleteContact(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')

    def dispatch(self, *args, **kwargs):
        return super(generic.DeleteView, self).dispatch(*args, **kwargs)
