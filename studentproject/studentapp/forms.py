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
		fields =['Name','Class','Admission_id','Gender','Nationality','Language','Category','Religion','Address','State','Country','Phone']
	helper = FormHelper()
	helper.form_method ='POST'
	helper.form_class = 'form-inline'
	helper.field_template = 'bootstrap3/layout/inline_field.html'
	helper.layout = Layout(
		'Name',
		'Class',
		'Admission_id',
		'Gender',
		'Nationality',
		'Language',
		'Category',
		'Religion',
		'Address',
		'State',
		'Country',
		'Phone',
		FormActions(Submit('Submit','Submit', css_class='btn-primary'))
		)





	
