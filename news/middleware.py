from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class CustomHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == "GET":
            content = response.content
            responses =  str.encode("<!—HelloWorld> </head>", encoding="UTF-8")
            content = content.replace(b"</head>", responses)
            response = HttpResponse(content)
        return response