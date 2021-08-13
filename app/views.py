from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from app.models import LogInfo


@method_decorator(login_required, name='dispatch')
class index(ListView):
    template_name = 'index.html'
    model = LogInfo
    context_object_name = 'records'

    def post(self, request, *args, **kwargs):
        login = self.request.user
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        workspace_number = int(request.POST['workspace_number'])
        worker = LogInfo(login=login, name=name, surname=surname, patronymic=patronymic, workspace_number=workspace_number)
        worker.save()
        return HttpResponseRedirect("/")