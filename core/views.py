from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ProfileForm

class Home(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request,'index.html')

@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    def get(self,request,*args,**kwargs):
        profiles=request.user.profiles.all()
        return render(request,'profileList.html',{'profiles':profiles})


class ProfileCreate(View):
    def get(self,request,*args,**kwargs):
        #form for creating profile
        form=ProfileForm()
        return render(request,'profileCreate.html',{'form':form})