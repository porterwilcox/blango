from django import template
register = template.Library()
from django.contrib.auth import get_user_model
user_model = get_user_model()
from django.utils.html import escape
from django.utils.safestring import mark_safe



@register.filter
def author_details(author):

    if not isinstance(author, user_model):
        return ""
    
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = author.username
    
    if author.email:
        # SECTION html injection attack!
        # email = '" onclick="alert(\'XSS\'); return false;' # the attack!
        # email = escape('" onclick="alert(\'XSS\'); return false;') # the fix!
        email = escape(author.email)
        prefix = f'<a href="mailto:{email}">'
        suffix = "</a>"
    else:
        prefix = ""
        suffix = ""

    return mark_safe(f"{prefix}{name}{suffix}")