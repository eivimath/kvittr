from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def user_register(request):
	context = {}
	if request.method == "POST":
		user = User()
		user.first_name = request.POST.get('firstname')
		user.last_name = request.POST.get('lastname')
		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.set_password(request.POST.get('password'))
		user.save()
		context['user_saved_successfully'] = True
	return render(request, 'useraccounts/register.html', context)