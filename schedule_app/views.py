from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_list_or_404

from schedule_app.models import Schedule


class IndexView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = 'schedule_app/index.html'
    login_url = 'auth/login/'

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_list_or_404(self.model, workers__user__first_name=self.request.user.first_name)
        return context
