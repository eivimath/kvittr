from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from messages_display.models import Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def messages(request):

	if request.method == "POST":
		new_message_text = request.POST.get('new_message')
		new_message = Message()
		new_message.message = new_message_text
		new_message.created_by = request.user
		new_message.created_datetime = timezone.now()
		new_message.save()

	messages = Message.objects.all()
	page_number = request.GET.get('page')
	paginator = Paginator(messages, 5)
	try:
		messages = paginator.page(page_number)
	except PageNotAnInteger:
		messages = paginator.page(1)
	except EmptyPage:
		messages = paginator.page(paginator.num_pages)

	context = {'messages': messages}
	return render(request, 'messages_display/messages.html', context)

def add_likes(request, message_id):
	message = Message.objects.get(pk=message_id)
	message.likes = message.likes + 1
	message.save()
	data = {'likes_updated': message.likes}
	return JsonResponse(data)

