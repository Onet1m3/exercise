from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.conf import settings
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class CustomHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == "GET":
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                content = response.content
                responses =  str.encode("<!—HelloWorld> </head>", encoding="UTF-8")
                content = content.replace(b"</head>", responses)
                response = HttpResponse(content)
            return response
        return response