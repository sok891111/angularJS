from django.shortcuts import get_object_or_404, render , render_to_response , redirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.utils import timezone
from django.http import JsonResponse
from django.template import RequestContext
from django.db.models import Q
from django.db import connection
from django.core.urlresolvers import reverse
from json import dumps
from .models import User

# Create your views here.

def login_form(request):
	return render(request, 'login/login.html')

def reg_form(request):
	return render(request, 'login/reg.html')

def reg(request):
	user = User.objects.create(
		user_email=request.POST['userEmail'],
		user_id = request.POST['userEmail'].split("@")[0],
		user_pw = request.POST['userPw'],
		user_name = request.POST['userName'],
		user_phone = request.POST['userPhone'],
		reg_date = timezone.now())
	user.save()
	return redirect('/login')

def check_id(request):
	try:
		user =User.objects.values('user_email').filter(pk=request.POST['userEmail'])
		result ={}
		if(user):
			result["allowed"] = False
		else:
			result["allowed"] = True
		response = JsonResponse(result)
	except Exception, e:
		print e.args[0]
	return response

def login(request):
	user=None
	user =User.objects.values('user_email', 'user_name','user_id').filter(
		pk=request.POST.get('userEmail',''),
		user_pw=request.POST.get('userPw',''))
	print user.query
	if not user.exists():
		result = {'message':'false'}
		return render(request, 'login/login.html',result)
	request.session['user'] = user[0]
	return redirect(reverse('home:home',kwargs={'user_id':user[0].get('user_id')}))

