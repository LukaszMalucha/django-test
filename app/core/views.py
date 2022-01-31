from django.shortcuts import render
from core.models import MessageModel


def home(request):

    messages = MessageModel.objects.all()

    return render(request, "home.html", {"messages": messages})



def failed_response(request, error_message, status):
    # Return an error message
    return render(request, 'myapp/login_failed.html', {
        'error_message': error_message,
    }, status=status)