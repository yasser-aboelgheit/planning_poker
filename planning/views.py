from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
import random


class CreateTicketView(TemplateView):
    template_name = 'planning/index.html'

def create_ticket_view(request, *args, **kwargs):

    TicketTitle = request.POST.get("TicketTitle")
    TicketRating = request.POST.get("TicketRating") or "0,1/2,1,2,3,5,8,13"

    return redirect(reverse('poll_view', kwargs={'pk': random.randrange(0,9)}) + '?TicketTitle=' + str(TicketTitle) + '&TicketRating=' + str(TicketRating))


class PollView(TemplateView):
    template_name = 'planning/poll.html'
