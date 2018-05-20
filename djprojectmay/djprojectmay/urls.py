"""djprojectmay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#Add this in for the function views
from bookstore import views
#Add in the BookLIst so that URLS knows where its coming from
from bookstore.views import BookList

#AUTH VIEWS
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^books/$', BookList.as_view()),
	url(r'^female_books/$', views.female_books, name='female_books'),
	#lets create A URL for TOP 5 Star Books
	url(r'five/$', views.five_star, name='five_star'),
	
	#Login, Logout, Signup Credentials.
	url(r'^login/$', auth_views.login, {'template_name': 'bookstore/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	#Created a FORM for USERS to add books on the User interface
	url(r'^bookform/$', views.bookform, name='bookform'),
    url(r'^admin/', admin.site.urls),
]
