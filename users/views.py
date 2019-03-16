from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



def register(request):
	if request.method == 'POST':		
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()							#will hash password and secure save form as new user
			username = form.cleaned_data.get('username') 
			messages.success(request, f'Your account has been created! You can now log in!')
			return redirect('login') 		#when a user creates a valid user account, they will get redirected to login
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		update_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if update_form.is_valid() and profile_form.is_valid():
			update_form.save()
			profile_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile') 
	else:
		update_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'update_form': update_form,
		'profile_form': profile_form
	}

	return render(request, 'users/profile.html', context)




