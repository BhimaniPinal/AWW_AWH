from django.shortcuts import render
from django.contrib.auth import views

class HomePage(views.TemplateView):
	template_name = "aww/home.html"
	pass;

class SubscribeUser(views.TemplateView):
	template_name = "aww/subscribe.html"
	pass;

class ListCirculars(views.TemplateView):
	template_name = "aww/circulars.html"
	pass;

class ListVacancies(views.TemplateView):
	template_name = "aww/vacancies.html"
	pass;