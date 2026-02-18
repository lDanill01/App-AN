from django.db import models
from django.utils import timezone

class Calculadora_Dieta_Ruminantes(models.Model):
    # Dados do Cliente
    nome_cliente        = models.CharField(max_length=255)
    nome_fazenda        = models.CharField(max_length=255)
    data_criacao        = models.DateTimeField(default=timezone.now)
    
    # Dados dos Animais
    quantidade_animais  = models.IntegerField()
    peso_inicial        = models.FloatField(help_text="Peso em kg")
    peso_final          = models.FloatField(help_text="Peso em kg")
    fator_ganho_peso    = models.FloatField(help_text="Multiplicador para ganho de peso")
    
    # Dados de Nutrientes
    peso                = models.FloatField(null=True, blank=True)
    proteina            = models.FloatField(null=True, blank=True)
    energia             = models.FloatField(null=True, blank=True)
    fibra               = models.FloatField(null=True, blank=True)
    carboidrato         = models.FloatField(null=True, blank=True)
    gordura             = models.FloatField(null=True, blank=True)
    
    # Resultados
    resultado_final     = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Calculadora de Dieta para Ruminantes"
        verbose_name_plural = "Calculadoras de Dieta para Ruminantes"
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.nome_cliente} - {self.nome_fazenda}"
    
    def calcular_ganho_peso(self):
        """Calcula o ganho de peso total baseado no fator multiplicador"""
        if self.peso_inicial > 0:
            peso_unitario = (self.peso_final - self.peso_inicial) * self.fator_ganho_peso
            self.resultado_final = peso_unitario * self.quantidade_animais
            return self.resultado_final
        return None