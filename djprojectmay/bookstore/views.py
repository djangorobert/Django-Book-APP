# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#For the VIEWS GENERIC
from django.views.generic import ListView
from bookstore.models import Book, BookForm

#Imports for the Signup View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

#For LOGIN REQUIRED 
from django.contrib.auth.decorators import login_required

# Create your views here.
# A View that only querys Books created by Women its done using a Django Manager Class.
@login_required
def female_books(request):
	templates = 'bookstore/female_books.html'
	f = Book.female.all()
	context = {
		'f': f
	}
	return render(request, templates, context)
#A HOME Page
def home(request):
	templates = 'bookstore/home.html'
	context = {}
	return render(request, templates, context)
#A View using a Django Manager that displays a Table List of the Top Rated Books with only a 5 Star
@login_required
def five_star(request):
	templates = 'bookstore/five_star.html'
	five = Book.five.all()
	context = {
		'five': five
	}
	return render(request, templates,context)
	
	
#Added in this Generic Django Class View so you all can see how convenient they can really be
class BookList(ListView):
	
	queryset = Book.male.all()
	
	
#The Signup VIEW
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'bookstore/signup.html', {'form': form})

#A Django Form to allow Users the ability to add in books of there own on the User Interface	
@login_required	
def bookform(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			title = form.cleaned_data['title']
			author = form.cleaned_data['author']
			
			gender = form.cleaned_data['gender']
			rating = form.cleaned_data['rating']
			return redirect('home')
	else:
		form = BookForm()
	return render(request, 'bookstore/bookform.html', {'form': form})
			