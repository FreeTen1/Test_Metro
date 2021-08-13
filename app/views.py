from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from app.models import LogInfo


@method_decorator(login_required, name='dispatch')
class index(ListView):
    template_name = 'index.html'
    model = LogInfo
    context_object_name = 'records'

    def post(self, request, *args, **kwargs):
        print(request.POST['name'], request.POST['surname'], request.POST['patronymic'], request.POST['workspace_number'])
        return super().get(request, *args, **kwargs)