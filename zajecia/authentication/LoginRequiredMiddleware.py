from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
import re
from django.utils.http import is_safe_url

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, "user"), "The Login Required Middleware"
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                redirect_to = settings.LOGIN_URL

                if len(path) > 0 and is_safe_url(
                    url=request.path_info, allowed_hosts=request.get_host()):
                    redirect_to = "%s?next=%s" % (redirect_to, request.path_info)
                return HttpResponseRedirect(redirect_to)
