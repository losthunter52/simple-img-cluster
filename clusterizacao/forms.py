from django.forms import ModelForm
from .models import Imagem

class ImagemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImagemForm, self).__init__(*args, **kwargs)
        self.fields['imagem'].label = 'Qual o nome da imagem?'
        self.fields['clusters'].label = 'Quantas cores(clusters) você quer utilizar?'
        self.fields['img'].label = 'Upload de Imagem (Utilize os formatos .jpeg ou .jpg)'

    class Meta:
        model = Imagem
        fields = '__all__'