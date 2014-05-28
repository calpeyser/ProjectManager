from django.db import models


class User(models.Model):
	name             = models.CharField(max_length = 50, unique = True);
	password         = models.CharField(max_length = 50);
	is_manager       = models.BooleanField(default=False);
	is_sales_agent   = models.BooleanField(default=False);
	is_artist        = models.BooleanField(default=False);
	is_sales_manager = models.BooleanField(default=False);

	def __unicode__(self):
		return unicode(self.name)

class Label(models.Model):	
	style         = models.CharField(max_length=100);
	garment_color = models.CharField(max_length=100);
	placement     = models.CharField(max_length=100);
	design_color  = models.CharField(max_length=100);

	def __unicode__(self):
		return unicode("Style: " + self.style + " Garment Color: " + self.garment_color + " Placement: " + self.placement + " Design Color: " + self.design_color)


class Project(models.Model):
	agent            = models.ForeignKey(User, related_name="agent_of", blank=True, null=True);
	artist           = models.ForeignKey(User, related_name="artist_of", blank=True, null=True);
	due_date         = models.DateField(blank=True, null=True);
	customer_name    = models.CharField(max_length=300, blank=True, null=True);
	customer_number  = models.CharField(max_length=50, blank=True, null=True);
	market           = models.CharField(max_length=30, blank = True, null=True);
 	labels           = models.ManyToManyField(Label, related_name="labels_of");
 	submission_date  = models.DateField(blank=True);
 	project_type     = models.IntegerField();
 	status           = models.CharField(max_length=30, blank=True, null=True);


