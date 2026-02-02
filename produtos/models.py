from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Marca")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Especie(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Espécie")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Divisao(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Divisão")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Divisão"
        verbose_name_plural = "Divisões"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Linha(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Linha")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    
    class Meta:
        verbose_name = "Linha"
        verbose_name_plural = "Linhas"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    # id_produto é criado automaticamente pelo Django como 'id'
    nome_produto = models.CharField(max_length=200, verbose_name="Nome do Produto")
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.PROTECT, 
        related_name='produtos',
        verbose_name="Marca"
    )
    especie = models.ForeignKey(
        Especie, 
        on_delete=models.PROTECT, 
        related_name='produtos',
        verbose_name="Espécie"
    )
    divisao = models.ForeignKey(
        Divisao, 
        on_delete=models.PROTECT, 
        related_name='produtos',
        verbose_name="Divisão"
    )
    linha = models.ForeignKey(
        Linha, 
        on_delete=models.PROTECT, 
        related_name='produtos',
        verbose_name="Linha"
    )
    imagem = models.ImageField(
        upload_to='produtos/imagens/', 
        blank=True, 
        null=True,
        verbose_name="Imagem"
    )
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['-data_cadastro']
    
    def __str__(self):
        return f"{self.nome_produto} - {self.marca}"