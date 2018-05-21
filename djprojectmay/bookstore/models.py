# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
# Create your models here.
	
class GenderMaleManager(models.Manager):
	def get_queryset(self):
		return super(GenderMaleManager, self).get_queryset().filter(gender='M')
		
class GenderFemaleManager(models.Manager):
	def get_queryset(self):
		return super(GenderFemaleManager, self).get_queryset().filter(gender='F')
		
#Lets create some managers for Ratings 
class FiveStarRatingManager(models.Manager):
	def get_queryset(self):
		return super(FiveStarRatingManager, self).get_queryset().filter(rating=5)
		
class Book(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER = ( 
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)
	
	ONE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	
	RATING  = (
		(ONE, 'One'),
		(TWO, 'Two'),
		(THREE, 'Three'),
		(FOUR, 'Four'),
		(FIVE, 'Five'),
	)
	
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now=True)
	gender = models.CharField(
		max_length=2,
		choices=GENDER,
		null=True)
	rating = models.IntegerField(
		max_length =1,
		choices=RATING,
		null=True
	)
	objects = models.Manager()
	robert_objects = RobertManager()
	male = GenderMaleManager()
	female = GenderFemaleManager()
	five = FiveStarRatingManager()
	
	def __unicode__(self):
		return self.title
		
	
class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'gender', 'rating']
