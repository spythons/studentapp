from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.



def home(request):
	form = studentdetailsform(request.POST)
	if request.POST:
		form = studentdetailsform(request.POST)
		if form.is_valid():
			form.save()
			stud_display=studentdetails.objects.all()
			message ="Thanks you for registering"
			return render(request,'display.html',{'stud_display':stud_display})
		else:
			form = studentdetailsform()
			return render(request,'home.html',{'form':form})



	return render(request,'home.html',{'form':form})


def displaystudent(request):
	stud_display=studentdetails.objects.all()
	return render(request,'display.html',{'stud_display':stud_display})

# def updatestudent(request):
# 	form = studentdetailsform()
# 	article = studentdetails.objects.get(id=1)
#   	form1 = form(instance=article)
	
# 	return render(request,'update.html',{'form1':form1})

class updatestudent(UpdateView):
	model = studentdetails
	fields =['Admission_number','Admission_date','First_name','Middle_name','Last_name','Course_Batch','Date_of_birth','Gender','Blood_group','Birth_place','Nationality','Mother_tongue','Category','Religion','Address_line1','Address_line2','City','State']
	template_name = 'update.html'

	