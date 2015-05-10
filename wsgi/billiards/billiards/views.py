from django.shortcuts import render
def index(request):
	context = {
		'url': "/login",
		'no_nav': True
	}
	return render(request, 'index.html', context)


