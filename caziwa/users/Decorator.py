from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse, redirect
import json as simplejson
from functools import wraps
import json


def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.is_ajax():
            if not request.user.is_authenticated():
                return HttpResponse(json.dumps({'login_required': True}), mimetype='application/json')
        else:
            if request.user.is_authenticated():
                return view_func(request, *args, **kwargs)
            else:
                path = request.get_full_path()
                login_url = reverse('login')
                return redirect(path, login_url, 'next')
    return wrapper

# def login_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return view_func(request, *args, **kwargs)
#         json = simplejson.dumps({'not_authenticated': True})
#         return HttpResponse(json, content_type='application/json', )
#     return wrapper

#
# def login_required(_view_func):
#     def _view(request, *args, **kargs):
#         if 'user' in request.session:
#             return _view_func(request, *args, **kargs)
#         return HttpResponseRedirect(reverse('signup'))
#     return _view
#




