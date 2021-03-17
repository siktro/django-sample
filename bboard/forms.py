from django.forms import ModelForm

from .models import Bb

class BbModelForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'kind')