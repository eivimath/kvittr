from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'theme/frontpage.html')

def messages(request):
	return render(request, 'messages_display/templates/messages_display/messages.html')

def users(request):
    return render(request, 'theme/users.html')