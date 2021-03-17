from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Bb, Rubric
from .forms import BbModelForm

def index(request):
    rubrics = Rubric.objects.all()
    ctx = { 
        'bbs': Bb.objects.all(),
        'rubrics': rubrics
    }
    return render(request, 'bboard/index.html', ctx)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubricts = Rubric.objects.all()
    cur_rubric = Rubric.objects.get(pk=rubric_id)

    ctx = {
        'bbs': bbs,
        'rubrics': rubricts,
        'cur_rubric': cur_rubric
    }

    return render(request, 'bboard/by_rubric.html', ctx)

class BbCreateView(generic.CreateView):
    template_name = 'bboard/create.html'
    form_class = BbModelForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['rubrics'] = Rubric.objects.all()
        return ctx