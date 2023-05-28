from django.views.generic import TemplateView, ListView
from web.models import Painting, Project
import random


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


class ContactView(TemplateView):
    template_name = 'contact.html'
