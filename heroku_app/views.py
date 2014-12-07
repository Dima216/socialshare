from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import JoinForm

def get_ip(request):
	try:
		x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forward:
			ip = x_forward
		else:
			ip = request.META.get('REMOTE_ADDR')
	except:
		ip = ''
	return ip

# Create your views here.
def home(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		new_join.ip_address = get_ip(request)
		new_join.save()
		return HttpResponseRedirect('%s'% new_join.id)

	context = {'form':form}
	template = 'home.html'
	return render(request, template, context)

def share(request, ref_id):
	#email = Join.objects.get(id=ref_id)

	context = {}
	template = 'home.html'
	return render(request, template, context)