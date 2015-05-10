from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
import logging

logger = logging.getLogger(__name__)

def index(request):
	if not request.session['user']:
		return redirect('/login')
	user_id = request.session['user'].get('user_id')
	return redirect(reverse('home:home',kwargs={'user_id':user_id}))
	
def home(request,user_id):
	if not request.session['user']:
		if request.session['user'].get('user_id') != user_id:
			return redirect('/login')
	return render(request, 'home/home.html')

class NgTemplate(TemplateView):

	def get_template_names(self):
		return ['home/views/%s.html' % self.kwargs['page']]

	def get_context_data(self,**kwargs):
		context = super(NgTemplate, self).get_context_data(**kwargs)
		return context

