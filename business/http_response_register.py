from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from adlink.forms import *
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
class HttpResponseRegister():
	def run(data):
		messages.success(request, "YEs")
		return HttpResponseRedirect('/login')
