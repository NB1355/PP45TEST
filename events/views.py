from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Event, Category

# Create your views here.


def all_events(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)

