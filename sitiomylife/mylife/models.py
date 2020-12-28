from django.db import models #desde django.db importamos los modelos
from django.utils import timezone

class Persona(models.Model):
    primer_nombre = models.CharField(max_length=10)
    mi_apellido = models.CharField(max_length=10)
    mi_edad = models.IntegerField(default=0)
    correo_email = models.EmailField(max_length=254)
    celular_telefono = models.IntegerField(default=0)
    mi_ciudad = models.CharField(max_length=20)
    codigo_postal = models.IntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.primer_nombre, self.mi_apellido)



class Publicacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_mio = models.CharField(max_length=10,default='')
    ciudad_mia = models.CharField(max_length=20,default='')
    mi_titulo = models.CharField(max_length=30)
    mi_texto = models.TextField(max_length=1000)
    mi_foto = models.ImageField(upload_to='media', null=True, blank=True)
    fecha_publicacion = models.DateTimeField('published_date')

    def __str__(self):
        return '{}'.format(self.nombre_mio)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    
class  Comment(models.Model):
    post = models.ForeignKey('mylife.Publicacion', on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)   

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.texto

    def approved_comment(self):
        return self.comments.filter(approved_comment=True)


