from functools import wraps
from django.http import HttpResponseForbidden

def permission_required_code(code: str):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return HttpResponseForbidden("Not authenticated.")

            
            if getattr(user, "is_super_admin", False):
                return view_func(request, *args, **kwargs)

            
            if hasattr(user, "has_perm_code") and user.has_perm_code(code):
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("you dont have permission for this action")
        return _wrapped
    return decorator
