from django.contrib import admin
from django.db import models 
from django.forms import CheckboxSelectMultiple

# Register your models here.

from .models import Icon, Person, Training_Session, Training_Spec

class PersonAdmin(admin.ModelAdmin):
	fields = ['first_name', 'last_name','slug','email','status','grad_year', 'committee', 'is_trainer']
	prepopulated_fields = {"slug": ("first_name", "last_name",)}
	list_display = ('slug', 'first_name', 'last_name', 'email','status', 'grad_year', 'committee', 'is_trainer')
	search_fields = ['first_name', 'last_name', 'grad_year', 'email']
	list_filter = ['status', 'grad_year', 'committee', 'is_trainer']

	def make_graduated(modeladmin, request, queryset):
		queryset.update(status='GRAD')
	def make_student(modeladmin, request, queryset):
		queryset.update(status='STU')
	def make_unknown(modeladmin, request, queryset):
		queryset.update(status='UNKNOWN')
	def toggle_committee(modeladmin, request, queryset):
		for person in queryset:
			if person.committee == False:
				setattr(person, 'committee', True)
			elif person.committee == True:
				setattr(person, 'committee', False)
			person.save() 
	def toggle_trainer(modeladmin, request, queryset):
		for person in queryset:
			if person.is_trainer == False:
				setattr(person, 'is_trainer', True)
			elif person.is_trainer == True:
				setattr(person, 'is_trainer', False)
			person.save() 

	actions = [make_graduated,make_student,make_unknown, toggle_committee, toggle_trainer]

class TrainingSpecAdmin(admin.ModelAdmin):
	list_filter = ['category']
	list_display = ['trainingId', 'category', 'trainingTitle', 'description', 'safety']

	def toggle_safety(modeladmin, request, queryset):
		for item in queryset:
			if item.safety == False:
				# item.update(safety=True)
				setattr(item, 'safety', True)
				item.save()  
			elif item.safety == True:
				# item.update(safety=False)
				setattr(item, 'safety', False)
				item.save()

	actions = [toggle_safety]

class TrainingSessionAdmin(admin.ModelAdmin):
	list_display = ['pk','trainer', '__str__', 'date',]
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
	}
	list_filter = ['date','trainee','trainer']

class IconAdmin(admin.ModelAdmin):
	prepopulated_fields = {"description": ("iconName",)}
	list_display = ['itemType', 'weight', 'iconName', 'iconRef']
	list_filter = ['itemType']

admin.site.register(Person, PersonAdmin)
admin.site.register(Training_Session, TrainingSessionAdmin)
admin.site.register(Training_Spec, TrainingSpecAdmin)
admin.site.register(Icon, IconAdmin)