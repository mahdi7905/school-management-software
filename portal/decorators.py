from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.http import HttpResponse





def  authenticatedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('portal')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowedUser(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def redirector(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == 'conventional head':
                return redirect('kia-head-teacher')
            if group == 'islamiya head':
                return redirect('islamiya-head')
            if group == 'kia admin':
                return redirect('kia-admin')
            if group == 'primary head':
                return redirect('sectional-head')
            if group == 'nursery head':
                return redirect('sectional-head')
            if group == 'pupils':
                return redirect('dashboard')
            if group == 'creator':
                return redirect('contentCreator')
            if group == 'islamiya teachers':
                return redirect('teachers-panel')
            if group == 'islamiya teachers':
                return redirect('page')
            if group == 'nursery teachers':
                return redirect('teachers-panel')
            if group == 'primary teachers':
                return redirect('teachers-panel')

        return view_func(request, *args, **kwargs)
    return wrapper_func