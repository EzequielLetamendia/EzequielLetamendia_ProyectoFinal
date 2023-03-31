from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    temporada = models.CharField(max_length=12)
    capitulo = models.CharField(max_length=50)
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    frase_o_escena = models.TextField(max_length=1000)
    creado_el = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''


    def __str__(self):
        return f"{self.id} - {self.temporada}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''


class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")