from django import forms
from .models import Calculadora_Dieta_Ruminantes

class CalculadoraDietaRuminantesForm(forms.ModelForm):
    class Meta:
        model = Calculadora_Dieta_Ruminantes
        fields = [
            'nome_cliente',
            'nome_fazenda',
            'quantidade_animais',
            'peso_inicial',
            'peso_final',
            'fator_ganho_peso',
            'proteina',
            'energia',
            'fibra',
            'carboidrato',
            'gordura'
        ]
        widgets = {
            'nome_cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do cliente'
            }),
            'nome_fazenda': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da fazenda'
            }),
            'quantidade_animais': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantidade de animais',
                'step': '1',
                'min': '1'
            }),
            'peso_inicial': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peso inicial (kg)',
                'step': '0.01',
                'min': '0'
            }),
            'peso_final': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peso final (kg)',
                'step': '0.01',
                'min': '0'
            }),
            'fator_ganho_peso': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fator multiplicador (ex: 1.5)',
                'step': '0.01',
                'min': '0'
            }),
            'proteina': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Proteína (%)',
                'step': '0.01',
                'min': '0',
                'required': False
            }),
            'energia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Energia (Mcal)',
                'step': '0.01',
                'min': '0',
                'required': False
            }),
            'fibra': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fibra (%)',
                'step': '0.01',
                'min': '0',
                'required': False
            }),
            'carboidrato': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Carboidrato (%)',
                'step': '0.01',
                'min': '0',
                'required': False
            }),
            'gordura': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Gordura (%)',
                'step': '0.01',
                'min': '0',
                'required': False
            }),
        }
        labels = {
            'nome_cliente': 'Nome do Cliente',
            'nome_fazenda': 'Nome da Fazenda',
            'quantidade_animais': 'Quantidade de Animais',
            'peso_inicial': 'Peso Inicial (kg)',
            'peso_final': 'Peso Final (kg)',
            'fator_ganho_peso': 'Fator de Ganho de Peso',
            'proteina': 'Proteína (%)',
            'energia': 'Energia (Mcal)',
            'fibra': 'Fibra (%)',
            'carboidrato': 'Carboidrato (%)',
            'gordura': 'Gordura (%)',
        }
