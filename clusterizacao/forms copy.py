from django import forms
from .models import Imagem

class ImagemForm(forms.models.ModelForm):
    img_original = forms.ImageField(required=True)

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = Imagem
        fields = ('nome', 'img_original')

        help_texts = {
        'img_original': 'either upload a new image, or choose from the gallery'
        }