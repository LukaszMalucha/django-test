from django.shortcuts import render
from core.models import MessageModel


def home(request):

    messages = MessageModel.objects.all()

    return render(request, "home.html", {"messages": messages})
