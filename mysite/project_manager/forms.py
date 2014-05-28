from django import forms
from django.forms import ModelForm
from project_manager.models import Label, Project, User
import datetime

class AuthForm(forms.Form):
	username = forms.CharField(max_length=50);
	password = forms.CharField(max_length=50);

class LabelForm(ModelForm):
	class Meta:
		model = Label

class TypeForm(forms.Form):
	Project_Type = forms.ChoiceField(choices=[
		('1', 'Simple logo placement'),
		('2', 'Modify drop-in concept and placement'),
		('3', 'Customer specific'),
		('4', 'Market specific art package'),
		('5', 'Corporate logo treatment presentation')
		])
	Number_Of_Lines = forms.IntegerField();

class ProjectForm1(forms.Form):
	customer_name    = forms.CharField(max_length=50);
	customer_number = forms.CharField(max_length=50);
	market           = forms.ChoiceField(choices = [
		('resort', 'resort'),
		('college', 'college'),
		('ASI', 'ASI'),
		('military', 'military'),
		('golf', 'golf')
		])
	due_date         = forms.DateField(input_formats=['%Y-%m-%d'], help_text="YYYY-MM-DD");

class ProjectForm2(forms.Form):
	customer_name    = forms.CharField(max_length=50);
	customer_number = forms.CharField(max_length=50);
	market           = forms.ChoiceField(choices = [
		('resort', 'resort'),
		('college', 'college'),
		('ASI', 'ASI'),
		('military', 'military'),
		('golf', 'golf')
		])
	due_date         = forms.DateField(input_formats=['%Y-%m-%d'], help_text="YYYY-MM-DD");

class ProjectForm3(forms.Form):
	customer_name    = forms.CharField(max_length=50);
	customer_number = forms.CharField(max_length=50);
	market           = forms.ChoiceField(choices = [
		('resort', 'resort'),
		('college', 'college'),
		('ASI', 'ASI'),
		('military', 'military'),
		('golf', 'golf')
		])
	due_date         = forms.DateField(input_formats=['%Y-%m-%d'], help_text="YYYY-MM-DD");

class ProjectForm4(forms.Form):
	customer_name    = forms.CharField(max_length=50);
	customer_number = forms.CharField(max_length=50);
	market           = forms.ChoiceField(choices = [
		('resort', 'resort'),
		('college', 'college'),
		('ASI', 'ASI'),
		('military', 'military'),
		('golf', 'golf')
		])
	due_date         = forms.DateField(input_formats=['%Y-%m-%d'], help_text="YYYY-MM-DD");

class ProjectForm5(forms.Form):
	customer_name    = forms.CharField(max_length=50);
	customer_number = forms.CharField(max_length=50);
	market           = forms.ChoiceField(choices = [
		('resort', 'resort'),
		('college', 'college'),
		('ASI', 'ASI'),
		('military', 'military'),
		('golf', 'golf')
		])
	due_date         = forms.DateField(input_formats=['%Y-%m-%d'], help_text="YYYY-MM-DD");

class EditForm1(ModelForm):
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market']

class EditForm1M(ModelForm):
	artist = forms.ModelChoiceField(queryset=User.objects.filter(is_artist=True), required=False)
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['artist', 'due_date', 'customer_name', 'customer_number', 'market', 'status']

class EditForm1A(ModelForm):
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market', 'status']


class EditForm2(ModelForm):
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market']

class EditForm2M(ModelForm):
	artist = forms.ModelChoiceField(queryset=User.objects.filter(is_artist=True))
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['artist', 'due_date', 'customer_name', 'customer_number', 'market', 'status']

class EditForm2A(ModelForm):
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market', 'status']


class EditForm3(ModelForm):
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market']

class EditForm3M(ModelForm):
	artist = forms.ModelChoiceField(queryset=User.objects.filter(is_artist=True))
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['artist', 'due_date', 'customer_name', 'customer_number', 'market', 'status']

class EditForm3A(ModelForm):
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market', 'status']


class EditForm4(ModelForm):
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market']

class EditForm4M(ModelForm):
	artist = forms.ModelChoiceField(queryset=User.objects.filter(is_artist=True))
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['artist', 'due_date', 'customer_name', 'customer_number', 'market', 'status']

class EditForm4A(ModelForm):
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market', 'status']


class EditForm5(ModelForm):
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market']

class EditForm5M(ModelForm):
	artist = forms.ModelChoiceField(queryset=User.objects.filter(is_artist=True))
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['artist', 'due_date', 'customer_name', 'customer_number', 'market', 'status']

class EditForm5A(ModelForm):
	status = forms.ChoiceField(choices = [
		('new', 'new'),
		('in-work', 'in-work'),
		('awaiting info', 'awaiting info'),
		('out for review', 'out for review'),
		('complete', 'complete'),
		('cancelled', 'cancelled')
		])
	class Meta:
		model = Project
		fields = ['due_date', 'customer_name', 'customer_number', 'market', 'status']


class EditLine(ModelForm):
	class Meta:
		model = Label;
