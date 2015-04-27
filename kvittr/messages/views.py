from django.shortcuts import render
from kvittr_messages.models import Message

# Create your views here.
def messages(request):
	messages = Message.objects.all()
	context = {'messages': messages}
	return render(request, 'messages/messages.html', context)