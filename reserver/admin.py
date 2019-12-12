from django.contrib import admin

from .models import Reservation
from accounts.models import User

class ReservationAdmin(admin.ModelAdmin):
    fields =['title','start_at','end_at','user']

admin.site.register(Reservation)