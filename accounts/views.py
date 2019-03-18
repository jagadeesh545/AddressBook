# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    """ Sign-up class to allow new users to create an account in the system"""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
