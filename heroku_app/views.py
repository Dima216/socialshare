from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.conf import settings
from models import Join
from forms import JoinForm
from uuid import uuid4

def get_ref_id(request):

	ref_id = str(uuid4())[:11].replace('-','').lower()
	return ref_id


def get_ip(request):
	try:
		x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forward:
			ip = x_forward.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
	except:
		ip = ''
	return ip

# Create your views here.
def home(request):
	try:
		refer_id = request.session['ref']
		obj = Join.objects.get(id=refer_id)
	except:
		obj = None
	
	print obj

	if request.method == 'POST':
		form = JoinForm(request.POST)
		if form.is_valid():
			new_join = form.save(commit=False)
			new_join.ip_address = get_ip(request)
			new_join.ref_id = get_ref_id(request)
			if not obj == None:
				new_join.friend = obj
				# Every joined will be has an obj as a friend.
			new_join.save()

			return HttpResponseRedirect('/%s'% (new_join.ref_id))
	else:
		form = JoinForm()

	context = {'form':form}
	template = 'home.html'
	return render(request, template, context)

def share(request, ref_id):
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		obj = Join.objects.filter(friend=join_obj)
		count = join_obj.Friend.all().count()
		ref_url = settings.SHARE_URL + str(join_obj.ref_id) 
		context = {'ref_id':join_obj.ref_id, 'count':count,'ref_url':ref_url}
		template = 'share.html'
		return render(request, template, context)
	except:
		raise Http404