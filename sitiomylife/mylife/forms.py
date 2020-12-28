# make sure this is at the top if it isn't already
from django import forms
from .models import Publicacion, Comment
from django.forms import ModelForm

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True,widget=forms.Textarea)


class ComentarioForm(forms.ModelForm):
    #mi_texto = forms.CharField(max_length=1000)
    #mi_titulo = forms.CharField(max_length=30)
    #content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Publicacion
        fields = ('mi_titulo', 'mi_texto' ,'mi_foto' , 'fecha_publicacion')



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('autor','texto')