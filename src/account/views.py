from django.shortcuts import render, HttpResponse
# to use built in django stuff
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User


# def user_login(request):
#     # why do we need forms?
#     # 1.to give data (form obj has cleaned_data field)
#     # 2.validations (form obj has .is_valid() method)
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             # auth checks user creds and returns user obj if they are correct 
#             # if auth was successful do...
#             if user is not None:
#                 # about .is_active: We recommend that you set this flag to False instead of deleting accounts
#                 if user.is_active: # why do we need use this check?
#                     login(request, user) # I thought login is a part of auth - haha I confused identification with authorization
#                     # login sets the user in current session
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account') # what is disabled account? it's like deleted
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,
                  'registration/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            # why do we need to set password using special function?
            # to hash password
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 
                      'registration/register.html', 
                      {'user_form': user_form})