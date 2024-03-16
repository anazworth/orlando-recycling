from .models import SearchLog


class SearchLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'q' in request.GET and request.GET['q'].strip():
            query = request.GET.get('q')
            SearchLog.objects.create(query=query)

        response = self.get_response(request)
        return response
