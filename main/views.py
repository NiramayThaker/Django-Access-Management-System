from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
@login_required(login_url="/login")
def index(request):
	return render(request, 'main/home.html')


def sign_up(request):
	# if we get post req we'll make new user Form
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)

			return redirect('/home')

	# else we will render the empty form on the screen
	else:
		form = RegisterForm()

	context = {"form": form}
	return render(request, 'registration/sign_up.html', context=context)
