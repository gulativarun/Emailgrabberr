from django.shortcuts import render,HttpResponseRedirect,Http404
from .forms import EmailForm,JoinForm
from .models import Join	
import uuid
# Create your views here.

def get_ip(request):

	try:

		x_forword = request.META.get("HTTP_X_FORWORDED_FOR")
		if x_forword :
			ip = x_forword.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	
	return ip


def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exsisted = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id

def share(request,ref_id):
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()
		ref_url = "http://127.0.0.1:8000/?ref=%s" %(join_obj.ref_id)
		context = {"ref_id" : join_obj.ref_id,"count":count,"ref_url":ref_url}
		template = "share.html"
		return render(request,template,context)
	except:
		raise Http404
	
def home(request):
	try:
		join_id = request.session['join_ref_id']
		obj = Join.objects.get(id=join_id)
		print obj.email
	except:
		obj = None   

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit= False)
		email = form.cleaned_data['email']
		new_join_old ,created = Join.objects.get_or_create(email=email)
		if created :
			new_join_old.ref_id = get_ref_id()
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()

		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		#new_join.ip_address = get_ip(request)
		#new_join.save()

	context = {"form" : form }
	template = "home.html"
	return render(request,template,context)