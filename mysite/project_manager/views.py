from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.template import Context, RequestContext
from project_manager.forms import *
from project_manager.models import User, Project
from utilities import *


global ROOT 
URL_ROOT = 'http://ec2-54-86-250-252.compute-1.amazonaws.com/'
#URL_ROOT = 'http://127.0.0.1:8000/'

def landing(request):
    if request.method == 'POST': 
        form = AuthForm(request.POST) 
        if form.is_valid(): 
			# validate that the user exists
			try:
				user = User.objects.filter(name = form.cleaned_data['username'])[0];
				notfound = False;
			except:
				user = form.cleaned_data['username'];
				notfound = True;
			if (notfound):
				status = "We're sorry, the username " + user + " does not exist."
				return render(request, 'project_manager/landing.html', {'form': form,'status': status})
			# validate that the password is good
			submitted_password = form.cleaned_data['password'];
			if (user.password == submitted_password):
				# multiplex based on type of user
				request.session["name"] = user.name
				if (user.is_sales_agent):
					return HttpResponseRedirect('/sales_home/')
				if (user.is_manager):
					return HttpResponseRedirect('/manager_home')
				if (user.is_artist):
					return HttpResponseRedirect('/artist_home/')
				if (user.is_sales_manager):
					return HttpResponseRedirect('/sales_manager_home')
			else:
				status = "We're sorry, the password you have entered does not match the username " + user.name
				return render(request, 'project_manager/landing.html', {'form': form,'status': status})
    else:
        form = AuthForm() # An unbound form

    status = "im a status!"
    return render(request, 'project_manager/landing.html', {
        'form': form,
        'status': status
    })

def go_home(request):
	return go_home_multiplex(request);

def sales_home(request):
	if not validId(request):
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; # assume unique names

	if request.method == 'POST': 
		form = TypeForm(request.POST) 
		if form.is_valid(): 
			return 	HttpResponseRedirect(URL_ROOT + 'create_project?lines=' + str(form.cleaned_data['Number_Of_Lines']) + '&type=' + str(form.cleaned_data['Project_Type']))

	else:
		form = TypeForm() # An unbound form

	return render(request, 'project_manager/sales_home.html/', {
		'form': form,
		'projects': Project.objects.filter(agent=current_user),
	})

def create_project(request):
	if not validId(request):
		return HttpResponseRedirect("/")

	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; # assume unique names


	if request.method == 'GET':
		lines = request.GET.get('lines')
		p_type = request.GET.get('type')
	elif request.method == 'POST':
		lines = request.POST.get('lines')
		p_type = request.POST.get('type')

	# make sure user isn't messing around...
	if lines == None:
		return HttpResponseRedirect('/sales_home/')	


	if request.method == 'POST':
		project_form = multiplex_form(p_type, request, True);
		if project_form.is_valid():
			save_project(request.POST, current_user);
			return HttpResponseRedirect(URL_ROOT + 'create_project')
	else:
		project_form = multiplex_form(p_type, request, False);


	return render(request, 'project_manager/create_project.html/', {
			'form': project_form,
			'type': p_type,
			'lines': lines,
			'lines_iter': range(int(lines)+1)[1:]
		})

def edit_project(request):
	if not validId(request):  # standard prologue
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0];

	# get the project in question
	try:
		if request.method == 'GET':
			this_project = Project.objects.filter(id=request.GET.get('project'))[0];
		elif request.method == 'POST':
			this_project = Project.objects.filter(id=request.POST.get('project'))[0];
	except:
		return HttpResponseRedirect('/')			
	if not this_project:
		return HttpResponseRedirect('/')	

	if request.method == 'POST':
		project_form = multiplex_form_edit(this_project.project_type, request, True, this_project, current_user.is_manager, current_user.is_artist);
		if project_form.is_valid():
			project_form.save()
			return HttpResponseRedirect(URL_ROOT + 'view_project?project=' + str(this_project.id))
	else:
		project_form = multiplex_form_edit(this_project.project_type, request, False, this_project, current_user.is_manager, current_user.is_artist);

	return render(request, 'project_manager/edit_project.html/', {'form': project_form, 'project': this_project, 'lines': this_project.labels.all()},)

def edit_line(request):
	if not validId(request):  # standard prologue
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0];

	# get the project in question
	try:
		if request.method == 'GET':
			this_project = Project.objects.filter(id=request.GET.get('project'))[0];
		elif request.method == 'POST':
			this_project = Project.objects.filter(id=request.POST.get('project'))[0];
	except:
		return HttpResponseRedirect('/')			
	if not this_project:
		return HttpResponseRedirect('/')
	# get the line in question	
	try:
		if request.method == 'GET':
			this_line = Label.objects.filter(id=request.GET.get('line'))[0];
		elif request.method == 'POST':
			this_line = Label.objects.filter(id=request.POST.get('line'))[0];
	except:
		return HttpResponseRedirect('/')			
	if not this_line:
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		project_form = EditLine(request.POST, instance=this_line)
		if project_form.is_valid():
			project_form.save()
			return HttpResponseRedirect(URL_ROOT + 'edit_project?project=' + str(this_project.id) + "&line=" + str(this_line.id))
	else:
		project_form = EditLine(instance=this_line)

	return render(request, 'project_manager/edit_line.html/', {'form': project_form, 'project': this_project, 'line': this_line})

def view_project(request):
	if not validId(request):  # standard prologue
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; 

	# get the project in question
	try:
		this_project = Project.objects.filter(id=request.GET.get('project'))[0];
		if not this_project:
			return HttpResponseRedirect('/')	
	except:
			return HttpResponseRedirect('/')	


	return render(request, 'project_manager/view_project.html/', {'project': this_project, 'labels': this_project.labels.all()})

def manager_home(request):
	if not validId(request):
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; 
	if not current_user.is_manager:
		return HttpResponseRedirect("/")

	# manager_home will display unallocated projects
	projects = Project.objects.filter(artist=None);
	return render(request, 'project_manager/manager_home.html', {'projects': projects})

def allocated_projects(request):
	if not validId(request):
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; 
	if not current_user.is_manager:
		return HttpResponseRedirect("/")

	all_projects = Project.objects.all();
	projects = filter(lambda x: x.artist != None, all_projects);
	return render(request, 'project_manager/allocated_projects.html', {'projects': projects})


def artist_home(request):
	if not validId(request):
		return HttpResponseRedirect("/")
	name = request.session['name'];
	current_user = User.objects.filter(name=name)[0]; 
	if not current_user.is_artist:
		return HttpResponseRedirect("/")

	projects = Project.objects.filter(artist=current_user)

	return render(request, 'project_manager/artist_home.html', {'projects': projects})

def sales_manager_home(request):
	if not validId(request):
		return HttpResponseRedirect("/")

	return render(request, 'project_manager/sales_manager_home.html')



