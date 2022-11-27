
import pandas as pd
import io
import urllib, base64

from matplotlib import pyplot as plt
from django.forms import model_to_dict
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django import forms
from django.utils import timezone
from app.forms import MyCommentForm, MyCommentFormchoices
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Paciente, Questionario
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
#from app.functions import SubirFoto
# Create your views here.

def loginUser(request):
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return lista(request)
    return render(request, 'lista.html', {})  


def logon(request):
    return render(request, "login2.html", {})


@login_required(login_url='../logon')
def logoutUser(request):
    logout(request) 
    return loginUser(request)

@login_required(login_url='../logon')
def index(request):
    return lista(request)



@login_required(login_url='../logon')
def lista(request):
    paciente = Paciente.objects.all()
    
    return render(request, 'lista.html', {'paciente': paciente})



class ListaPaciente(ListView):
    template_name = "lista.html"
    model = Paciente
    context_object_name = "paciente"



class PacienteUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Paciente
    fields = '__all__'
    context_object_name = 'paciente'
    success_url = reverse_lazy('lista_paciente')


class PacienteDeleteView(DeleteView):
    template_name = "exclui.html"
    model = Paciente
    fields = '__all__'
    context_object_name = 'paciente'
    success_url = reverse_lazy('lista_paciente')


class QuestionarioCreateView(CreateView):
    template_name = 'questionario.html'
    model = Questionario, Paciente
    fiels = '__all__'
    form_class = MyCommentFormchoices
    success_url = reverse_lazy('lista_paciente')

    


class PacienteCreateView(CreateView):
    template_name = 'cadastro2.html'
    model = Paciente
    fiels = '__all__'
    form_class = MyCommentForm
    success_url = reverse_lazy('lista_paciente')

# Get data_base

def DataBaseQuerySet(request):
    # Get database object django
    queryset = [model_to_dict(i) for i in Paciente.objects.all()]

    # Change queryset at DataFrame Pandas
    dataframe = pd.DataFrame(queryset)
    
    # Remove columns DataFrame
    dataframe = dataframe.drop(columns='foto')
    dataframe = dataframe.drop(columns='message')

    # Add new column frequencia
    dataframe['frequencia'] = dataframe.groupby('cidade')['cidade'].transform('count')

    # Plot a graphic and your size
    fig, ax = plt.subplots(figsize=(14,6))

    # Parameters of graphic
    bar_color = ['#FFE4C4', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1E90FF', '#00CED1',
          '#7CFC00', '#D2691E', '#9932CC', '#FFD700', '#FF6347']
    freq = dataframe['frequencia']
    cidade = dataframe['cidade']
    ax.set_ylabel("Qtd de Pacientes", fontsize = 15)
    ax.tick_params(axis= 'y', labelsize= 10)
    ax.tick_params(axis= 'x', labelsize= 8, rotation = 20)
    ax.set_facecolor("#d3d3d3")
    ax.set_yticks([1 * i for i in dataframe['frequencia']])
    ax.set_title("Cidades da Microrregião de Araraquara", fontsize = 16)
    ax.bar(cidade, freq, width=0.5, color=bar_color)

    # Parameters for show
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'analise.html', {'data' : uri }) 

   

def Imprimir(request, paciente_id):
    questionario = Questionario.objects.get(paciente_id=paciente_id)
    return render(request, 'imprimir.html', {'questionario' : questionario})
   
    
def SalvarFoto(request):
    if request.method == 'POST':
        post = Paciente.objects.get(all)
        form = MyCommentForm(request.POST, request.FILES)
        context = {
            'form': form,
            'post': post
                   
                   }
        if form.is_valid():
            form.save()
            return redirect('lista_paciente')
        else:
            form = MyCommentForm()
        return render(request,'cadastro2.html', context)

# def photo_create(request):
#     template_name = 'cadastro2.html'
#     form = FotoForm(request.POST or None)

#     if request.method == 'POST':
#         foto = request.FILES.getlist('photo')  # pega vários arquivos.

#         if form.is_valid():
#             paciente = form.save()
#     context = {'form': form}
#     return render(request, template_name, context)

def Questionariosave(request, paciente_id):
    questionario = Questionario()
    paciente = Paciente.objects.get(pk=paciente_id)
    if request.method == 'POST':
        questionario.paciente = paciente
        questionario.um = request.POST.get('um')
        questionario.dois = request.POST.get('dois')
        questionario.tres = request.POST.get('tres')
        questionario.quatro = request.POST.get('quatro')
        questionario.cinco = request.POST.get('cinco')
        questionario.seis = request.POST.get('seis')
        questionario.sete = request.POST.get('sete')
        questionario.oito = request.POST.get('oito')
        questionario.nove = request.POST.get('nove')
        questionario.dez = request.POST.get('dez')
        questionario.onze = request.POST.get('onze')
        questionario.doze = request.POST.get('dose')
        questionario.treze = request.POST.get('treze')
        questionario.quatorze = request.POST.get('quatorze')
        questionario.quinze = request.POST.get('quinze')
        questionario.desesseis = request.POST.get('desesseis')
        questionario.desessete = request.POST.get('desessete')
        questionario.dezoito = request.POST.get('dezoito')
        questionario.dezenove = request.POST.get('dezenove')
        questionario.vinte = request.POST.get('vinte')
        questionario.vinteum = request.POST.get('vinteum')
        questionario.vintedois = request.POST.get('vintedois')
        questionario.vintetres = request.POST.get('vintetres')  
        questionario.save()
        return redirect('lista_paciente')
        
    return render(request, 'questionario2.html',{'paciente':paciente})



# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = ExampleModel.objects.get(pk=id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#     return HttpResponseForbidden('allowed only via POST')