
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
# Create your views here.
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
#from app.functions import SubirFoto



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
    model = Questionario
    fiels = '__all__'
    form_class = MyCommentFormchoices
    success_url = reverse_lazy('lista_paciente')


        


class PacienteCreateView(CreateView):
    template_name = 'cadastro2.html'
    model = Paciente
    fiels = '__all__'
    form_class = MyCommentForm
    success_url = reverse_lazy('lista_paciente')



        

def Imprimir(request, paciente_id):
    questionario = Questionario.objects.get(paciente_id=paciente_id)
    return render(request, 'imprimir.html', {'questionario' : questionario})
   
    
def SalvarFoto(request):
    if request.method == 'POST':
        form = MyCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_paciente')
        else:
            form = MyCommentForm()
        return render(request,'cadastro2.html',{'form':form})

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