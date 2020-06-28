import re

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import is_safe_url
import jwt
from django.contrib.auth.models import User
from django.contrib.auth import login
import datetime


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required Middleware"

        path = request.path_info.lstrip('/')
        request.LANGUAGES = settings.LANGUAGES
        if not any(m.match(path) for m in EXEMPT_URLS):
            if 'HTTP_AUTHORIZATION' in request.META:
                token = request.META['HTTP_AUTHORIZATION']
                jwt_token = jwt.decode(token, 'test123')
                username = jwt_token['username']
                expire = jwt_token['expire']
                if expire < datetime.datetime.now().timestamp():
                    return HttpResponse(status=403)
                user = User.objects.get(username=username)

                login(request, user)

            elif not request.user.is_authenticated:
                    redirect_to = settings.LOGIN_URL
                    # 'next' variable to support redirection to attempted page after login
                    if len(path) > 0 and is_safe_url(
                        url=request.path_info, allowed_hosts=request.get_host()):
                        redirect_to = f"{settings.LOGIN_URL}?next={request.path_info}"

                    #return HttpResponse(status=403)
                    return HttpResponseRedirect(redirect_to)