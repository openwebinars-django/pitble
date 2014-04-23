class MyMiddleware(object):

    def process_request(self, request):
        import ipdb; ipdb.set_trace()
        try:
            request.section = Section.objects.get(slug=request.get_full_path().split('/')[0])
        except Section.DoesNotExists:
            request.section = None

    def process_view(self, request, view, *args, **kwargs):
        import ipdb; ipdb.set_trace()

    def process_exception(self, request, exception):
        import ipdb; ipdb.set_trace()

    def process_response(self, request, response):
        import ipdb; ipdb.set_trace()
        return response