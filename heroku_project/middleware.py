from heroku_app.models import Join

class ReferMiddleware():
	def process_request(self,request):
		ref_id = request.GET.get('ref')
		# print ref_id
		try:
			obj = Join.objects.get(ref_id=ref_id)
			# print obj
		except:
			obj = None
		if obj:
			request.session['ref'] = obj.id