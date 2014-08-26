from django import forms
from .models import *



class studentdetailsform(forms.ModelForm):
	# date = forms.DateField(widget=forms.TextInput(attrs={'class':'vDateField'}))
	class Meta:
		model = studentdetails
		fields =['Name','Class','Admission_id','Gender','Nationality','Language','Category','Religion','Address','State','Country','Phone']