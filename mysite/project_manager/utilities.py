from project_manager.forms import *
from project_manager.models import User, Project, Label
from django.http import HttpResponseRedirect, HttpResponse
from datetime import date

def validId(request):
	if 'name' in request.session:
		return True
	return False

def multiplex_form(t, request, is_bound):
	if t == "1":
		if is_bound:
			return ProjectForm1(request.POST);
		else: 
			return ProjectForm1();
	if t == "2":
		if is_bound:
			return ProjectForm2(request.POST);
		else: 
			return ProjectForm2();
	if t == "3":
		if is_bound:
			return ProjectForm3(request.POST);
		else: 
			return ProjectForm3();
	if t == "4":
		if is_bound:
			return ProjectForm4(request.POST);
		else: 
			return ProjectForm4();
	if t == "5":
		if is_bound:
			return ProjectForm5(request.POST);
		else: 
			return ProjectForm5();

def multiplex_form_edit(t, request, is_bound, instance, is_manager, is_artist):
	if t == 1:
		if is_bound:
			if is_manager:
				return EditForm1M(request.POST, instance=instance)
			elif is_artist:
				return EditForm1A(request.POST, instance=instance)
			else:
				return EditForm1(request.POST, instance=instance);
		else: 
			if is_manager:
				return EditForm1M(instance=instance)
			elif is_artist:
				return EditForm1A(instance=instance)
			else:
				return EditForm1(instance=instance);
	if t == 2:
		if is_bound:
			if is_manager:
				return EditForm2M(request.POST, instance=instance)
			elif is_artist:
				return EditForm2A(request.POST, instance=instance)
			else:
				return EditForm2(request.POST, instance=instance);
		else: 
			if is_manager:
				return EditForm2M(instance=instance)
			elif is_artist:
				return EditForm2A(instance=instance)
			else:
				return EditForm2(instance=instance);
	if t == 3:
		if is_bound:
			if is_manager:
				return EditForm3M(request.POST, instance=instance)
			elif is_artist:
				return EditForm3A(request.POST, instance=instance)
			else:
				return EditForm3(request.POST, instance=instance);
		else: 
			if is_manager:
				return EditForm3M(instance=instance)
			elif is_artist:
				return EditForm3A(instance=instance)
			else:
				return EditForm3(instance=instance);
	if t == 4:
		if is_bound:
			if is_manager:
				return EditForm4M(request.POST, instance=instance)
			elif is_artist:
				return EditForm4A(request.POST, instance=instance)
			else:
				return EditForm4(request.POST, instance=instance);
		else: 
			if is_manager:
				return EditForm4M(instance=instance)
			elif is_artist:
				return EditForm4A(instance=instance)
			else:
				return EditForm4(instance=instance);
	if t == 5:
		if is_bound:
			if is_manager:
				return EditForm5M(request.POST, instance=instance)
			elif is_artist:
				return EditForm5A(request.POST, instance=instance)
			else:
				return EditForm5(request.POST, instance=instance);
		else: 
			if is_manager:
				return EditForm5M(instance=instance)
			elif is_artist:
				return EditForm5A(instance=instance)
			else:
				return EditForm5(instance=instance);

def save_project(data, current_user):
	number_of_lines = int(data['lines']);
	labels = [];
	for i in range(number_of_lines+1)[1:]:
		style = data['Style' + str(i)];
		garment = data['Garment' + str(i)];
		placement = data['Placement' + str(i)];
		design = data['Design' + str(i)];
		new_label = Label(style=style, garment_color=garment, placement=placement, design_color=design);
		new_label.save();
		labels.append(new_label);
	new_project = Project(agent=current_user, due_date=data['due_date'], customer_name=data['customer_name'], customer_number=data['customer_number'], market=data['market'], submission_date=date.today(), project_type=data['type'], status="new");
	new_project.save()
	for l in labels:
		new_project.labels.add(l)

def go_home_multiplex(request):
	if not validId(request):
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; # assume unique names
	if current_user.is_sales_agent:
		return HttpResponseRedirect('/sales_home/')
	if current_user.is_manager:
		return HttpResponseRedirect('/manager_home/')
	if current_user.is_artist:
		return HttpResponseRedirect('/artist_home/')
	if current_user.is_sales_manager:
		return HttpResponseRedirect('/sales_manager_home/')




