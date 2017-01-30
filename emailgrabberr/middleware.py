from joins.models import Join
class RefMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ref_id = request.GET.get("ref",'')
        print ref_id
        try:            
            obj = Join.objects.get(ref_id = ref_id)        	
            print obj
        except:
        	obj = None
        if obj:
            request.session['join_ref_id'] = obj.id
                   
        response = self.get_response(request)
        return response