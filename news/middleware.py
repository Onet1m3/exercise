from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class CoolMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        content = response.rendered_content
        content = content.replace('</head>', ' <!—HelloWorld> </head>')
        response = HttpResponse(content, content_type="text/html")
        return response
