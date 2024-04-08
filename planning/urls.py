from django.urls import path
from .views import CreateTicketView, PollView, create_ticket_view


urlpatterns = [
    path("", CreateTicketView.as_view(), name="create_ticket_view"),
    path("poll/<int:pk>/", PollView.as_view(), name="poll_view"),
    path("create_ticket/", create_ticket_view, name="create_ticket_view"),
]
