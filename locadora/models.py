from django.db import models

class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nome
class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome
class Locacao (models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nome} - {self.data}"
class Filme (models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    locacao = models.ManyToManyField (Locacao)
    def __str__(self) -> str:
        return self.titulo