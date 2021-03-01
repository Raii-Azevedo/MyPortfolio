from django.views.generic import TemplateView
from .models import Sobre, Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sobres'] = Sobre.objects.all()
        context['servicos'] = Servico.objects.order_by('?').all()
        return context

