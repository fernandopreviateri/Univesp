"""univesp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib import admin
from django.urls import URLPattern, path
from app.views import  ListaPaciente, PacienteUpdateView, PacienteDeleteView, PacienteCreateView, QuestionarioCreateView, DataBaseQuerySet




app_name = 'paciente'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.logon, name="logon"),
    path('login', views.loginUser, name="login"),
    path('index/', views.index, name="index"),
    path('lista/', ListaPaciente.as_view(), name="lista_paciente"),
    path('atualiza/<pk>', PacienteUpdateView.as_view(), name="atualiza_paciente"),
    path('cadastro/exclui/<pk>', PacienteDeleteView.as_view(), name="exclui_paciente"),
    path('cadastro/', PacienteCreateView.as_view(), name="cadastro_paciente"),
    path('cadastro/<paciente_id>', views.Questionariosave, name="questionario"),
    path('cadastro/<paciente_id>', QuestionarioCreateView.as_view(), name="cadastro_paciente"),
    path('analise/', views.DataBaseQuerySet, name='analise'),
    path('imprimir/<paciente_id>', views.Imprimir, name="imprimir"),
    #path('cadastro/' , views.SalvarFoto, name="foto"),
    #path('cadastro/lista/', ListaPaciente.as_view(), name="lista_paciente"),
   
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT,
#     )

