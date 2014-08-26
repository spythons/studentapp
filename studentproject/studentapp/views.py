from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.



def home(request):
	form = studentdetailsform(request.POST)
	if request.POST:
		form = studentdetailsform(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'thanks.html')
		else:
			form = studentdetailsform()
			return render(request,'home.html',{'form':form})



	return render(request,'home.html',{'form':form})