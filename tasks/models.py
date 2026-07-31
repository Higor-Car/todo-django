from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome