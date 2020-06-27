from django.shortcuts import render
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! YOu are now able to login!')
            return redirect('item-list')
    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html',{'form':form})


@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() :
            u_form.save()
            # p_form.save()
            messages.success(request,f'Your account has been Updated!')
            return redirect('account')
    else:
        u_form = UserUpdateForm(instance = request.user)
        # p_form = ProfileUpdateForm(instance = request.user.profile)
    
    context = {
        'u_form':u_form,
        # 'p_form':p_form
    }
    return render(request, 'user/account.html',context)


def deals(request):
    return render(request, 'user/deals.html')

def clothes(request):
    return render(request, 'user/clothes.html')

def shoes(request):
    return render(request, 'user/shoes.html')

def help(request):
    return render(request, 'user/help.html')