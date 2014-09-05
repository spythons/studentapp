from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Field,Layout
from crispy_forms.bootstrap import (AppendedText,PrependedText,FormActions,InlineField)
from django.forms.extras.widgets import SelectDateWidget


class studentdetailsform(forms.ModelForm):
	# date = forms.DateField(widget=forms.TextInput(attrs={'class':'vDateField'}))
	class Meta:
		model = studentdetails
		fields =['Admission_number','Admission_date','First_name','Middle_name','Last_name','Course_Batch','Date_of_birth','Gender','Blood_group','Birth_place','Nationality','Mother_tongue','Category','Religion','Address_line1','Address_line2','City','State']
	helper = FormHelper()
	helper.form_method ='POST'
	helper.form_class = 'form-inline'
	helper.field_template = 'bootstrap3/layout/inline_field.html'
	helper.layout = Layout(
		'Admission_number',
		'Admission_date',
		'First_name',
		'Middle_name',
		'Last_name',
		'Course_Batch',
		'Date_of_birth',
		'Gender',
		'Blood_group',
		'Birth_place',
		'Nationality',
		'Mother_tongue',
		'Category',
		'Religion',
		'Address_line1',
		'Address_line2',
		'City',
		'State',
		FormActions(Submit('Submit','Submit', css_class='btn-primary'))
		)





	
