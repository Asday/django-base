from django.http import HttpResponse
from django.views.generic import View


class PrivateFile(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("wow")
