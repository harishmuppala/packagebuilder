from django.db import models

class Package(models.Model):
	random_id = models.CharField(db_index=True,max_length=255, blank=True)
	created_date = models.DateTimeField(null=True,blank=True)
	finished_date = models.DateTimeField(null=True,blank=True)
	username = models.CharField(max_length=255)
	api_version = models.CharField(max_length=255)
	package = models.TextField(blank=True)
	status = models.CharField(max_length=255, blank=True)
	error = models.TextField(blank=True)

	def sorted_component_types(self):
		return self.componenttype_set.order_by('name')

class ComponentType(models.Model):
	package = models.ForeignKey(Package)
	name = models.CharField(max_length=255)
	include_all = models.BooleanField(default=True)

	def sorted_components(self):
		return self.component_set.order_by('name')

class Component(models.Model):
	component_type = models.ForeignKey(ComponentType)
	name = models.CharField(max_length=255)
	include = models.BooleanField(default=True)
