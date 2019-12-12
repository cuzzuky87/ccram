from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Reservation

class Top(LoginRequiredMixin,ListView):
    template_name = 'reserver/top.html'
    model = Reservation
    context = "reservation"
