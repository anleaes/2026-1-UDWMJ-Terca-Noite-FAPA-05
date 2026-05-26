from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from .utils import LOGIN_URL, user_is_client, user_is_employee


def employee_required(view_func):
    @login_required(login_url=LOGIN_URL)
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not user_is_employee(request.user):
            if user_is_client(request.user):
                return redirect('core:home')
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper
