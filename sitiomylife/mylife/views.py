from django.shortcuts import render, redirect
from .models import Publicacion, Persona , Comment
#from django.views import generic
from django.utils import timezone
from django.shortcuts import  get_object_or_404
#nuevo
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
# add to the top
from mylife.forms import ContactForm, CommentForm

from mylife.forms import ComentarioForm
from django.forms import ModelForm
from django.template import RequestContext

from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

#def index(request):
    #latest_question_list = Publicacion.objects.all()
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'mylife/index.html', context)

#class IndexView(generic.ListView):
    #template_name = 'mylife/index.html'
    #context_object_name = 'latest_question_list'

def index(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    if request.user.is_authenticated:
        return render(request, 'mylife/index.html', {'posts': posts} )
    return redirect("/login")
    


  
def post_detail(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'mylife/post_detail.html', {'post': post})


#def image(request):
#post = Publicacion.objects.all()
    #for mycar in post:
        #MyCar = mycar.mi_foto.url
        #variables = RequestContext(request,{'post':MyCar })
       # return render_to_response('index.html',variables)


    #def get_queryset(request ):
        #"""Return the last five published questions."""
       # return Publicacion.objects.order_by()
       

#class DetailView(generic.DetailView):
   # model = Publicacion
    #template_name = 'mylife/detalle.html'

def welcome(request):
    if request.user.is_authenticated: # si estamos identificados devolvemos la portada
        return render(request, "mylife/index.html")
    return redirect("/login") # si no redireccionamos al login


def register(request):
    form = UserCreationForm()# Creamos el formulario de autenticación vacío
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)# Añadimos los datos recibidos al formulario
        if form.is_valid(): # Si el formulario es válido...
            user = form.save() # Creamos la nueva cuenta de usuario
            if user is not None: # Si el usuario se crea correctamente
                do_login(request, user)  # Hacemos el login manualmente
                return redirect('/')# Y le redireccionamos a la portada
    return render(request, "mylife/register.html", {'form': form}) # Si llegamos al final renderizamos el formulario


def login(request):
    form = AuthenticationForm() # creamos el formulario de autentificacion
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)# AÑADIMOS los datos recibidos al form
        if form.is_valid(): # si el form es valido
            username = form.cleaned_data['username'] # recuperamos la credenciales validas
            password = form.cleaned_data['password'] # recuperamos la credenciales validas
            user = authenticate(username=username,password=password) #verificamos las credenciales del user
            if user is not None: # si existe un user con ese nombre y password
                do_login(request, user) # hacemos el login manualmente
                return redirect('/')

    return render(request, 'mylife/login.html', {'form':form}) # si llegamos al final renderizamos el formulario


def logout(request):
    do_logout(request)  #finalizamos la secion
    return redirect('/')  #redireccionamos ala portada


def quienessomos(request):
    return render(request, 'mylife/quienessomos.html')



def contacto(request):
    form_class = ContactForm
    return render(request, 'mylife/contacto.html', {'form': form_class,})




#formulario = form.save(commit=False)




def post_new(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'mylife/post_detail.html', {'form': form})




def post_edit(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ComentarioForm(instance=post)
    return render(request, 'mylife/post_edit.html', {'form': form})




def add_comment_to_post(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'mylife/add_comment_to_post.html', {'form': form} )


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)





