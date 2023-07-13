from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from web.models import Painting, Project
from django.conf import settings
import random
import os


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paintings = Painting.objects.all()
        if paintings:
            context['painting'] = random.choices(Painting.objects.all())[0]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ProjectsView(ListView):
    template_name = 'projects.html'
    queryset = Project.objects.order_by('priority')
    context_object_name = 'projects'


class ProjectView(DetailView):
    template_name = 'project.html'
    model = Project
    context_object_name = 'project'


class ContactView(TemplateView):
    template_name = 'contact.html'


class ReloadView(LoginRequiredMixin, UserPassesTestMixin, RedirectView):
    to = "/"

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        os.system(settings.BASE_DIR / "update.sh")
        return super().get(*args, **kwargs)
