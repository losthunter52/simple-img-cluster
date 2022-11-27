from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagem
from .forms import ImagemForm
from main import settings
from django.views.generic import ListView, DetailView
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from sklearn.cluster import KMeans

# Generico

def index(request):
    num_imagens = Imagem.objects.all().count()

    context = {
        'num_imagens': num_imagens,
    }
    template_name = 'home.html'
    return render(request, template_name, context) 

# Imagem

class listaImagem(ListView):
    template_name = 'listaImagem.html'
    context_object_name = 'imagem_list'

    def get_queryset(self):
        return Imagem.objects.all()    

class detalhesImagem(DetailView):
    model = Imagem
    template_name ='detalhesImagem.html'

def cadastroImagem(request):
    form = ImagemForm()
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            Imagem = form.save()

            img_arr = img.imread(Imagem.img)

            (h,w,c) = img_arr.shape

            img2D = img_arr.reshape(h*w,c)

            kmeans_model = KMeans(n_clusters=int(Imagem.clusters), init="random")
            clusters_labels = kmeans_model.fit_predict(img2D)

            centroid = kmeans_model.cluster_centers_

            rgb_colors = centroid.round(0).astype(int)

            labels = (kmeans_model.labels_)

            img_quant = np.reshape(rgb_colors[clusters_labels],(h,w,c))

            labels=list(kmeans_model.labels_)

            percent=[]
            for i in range(len(centroid)):
                j=labels.count(i)
                j=j/(len(labels))
                percent.append(j)
                print(percent)

            fig, ax = plt.subplots(1,3, figsize=(20,12))
            ax[0].imshow(img_arr)
            ax[0].set_title('Imagem Original')
            ax[1].imshow(img_quant)
            ax[1].set_title('Imagem Quantizada')
            ax[2].pie(percent,colors=np.array(centroid/255),labels=np.arange(len(centroid)))
            ax[2].set_title('Paleta de cores')
            imagem_name = str(Imagem.img).split('/')[1]

            fig.savefig(str(settings.MEDIA_ROOT) + '/uploads/' + imagem_name)
            return redirect('ImagemDetalhes', Imagem.pk)
        else:
            print(request.FILES)

    return render(request,'cadastro.html',{'form': form})

def excluirImagem(request, pk, template_name='confirm_delete.html'):
    imagem = get_object_or_404(Imagem, pk=pk)
    if request.method=='POST':
        imagem.delete()
        return redirect('Imagem')
    return render(request, template_name, {'object':imagem})