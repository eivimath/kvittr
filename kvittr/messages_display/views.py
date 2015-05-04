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

def like_button(request):
    like = Like.objects.get(pk=0)
    messages.liked =  messages.liked + 1
    messages.save()
    data = {'likes_updated': messages.likes}
    return JsonResponse(data)