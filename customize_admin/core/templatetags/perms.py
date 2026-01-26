from django import template

register = template.Library()

@register.filter
def has_perm_code(user, code):
    if not user or not getattr(user, "is_authenticated", False):
        return False
    if getattr(user, "is_super_admin", False):
        return True
    fn = getattr(user, "has_perm_code", None)
    return fn(code) if callable(fn) else False

