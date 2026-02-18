from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Calculadora_Dieta_Ruminantes
from .forms import CalculadoraDietaRuminantesForm

class CalculadoraDietaListView(LoginRequiredMixin, ListView):
    """Lista todas as calculadoras de dieta registradas"""
    model = Calculadora_Dieta_Ruminantes
    template_name = 'calculadoras/calculadora_list.html'
    context_object_name = 'calculadoras'
    paginate_by = 10
    
    def get_queryset(self):
        return Calculadora_Dieta_Ruminantes.objects.all().order_by('-data_criacao')

class CalculadoraDietaDetailView(LoginRequiredMixin, DetailView):
    """Exibe os detalhes e resultados de uma calculadora específica"""
    model = Calculadora_Dieta_Ruminantes
    template_name = 'calculadoras/calculadora_detail.html'
    context_object_name = 'calculadora'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calculadora = self.get_object()
        # Recalcular resultado ao visualizar
        if calculadora.peso_inicial and calculadora.peso_final and calculadora.fator_ganho_peso:
            calculadora.calcular_ganho_peso()
        context['resultado_total'] = calculadora.resultado_final
        return context

class CalculadoraDietaCreateView(LoginRequiredMixin, CreateView):
    """Cria uma nova calculadora de dieta de ruminantes"""
    model = Calculadora_Dieta_Ruminantes
    form_class = CalculadoraDietaRuminantesForm
    template_name = 'calculadoras/calculadora_form.html'
    success_url = reverse_lazy('calculadora_list')
    
    def form_valid(self, form):
        calculadora = form.save(commit=False)
        # Executar cálculo antes de salvar
        calculadora.calcular_ganho_peso()
        calculadora.save()
        return redirect(self.success_url)

def calculadora_dieta(request):
    """View para calcular dieta de ruminantes com teste básico"""
    resultado = None
    form = CalculadoraDietaRuminantesForm()
    
    if request.method == 'POST':
        form = CalculadoraDietaRuminantesForm(request.POST)
        if form.is_valid():
            calculadora = form.save(commit=False)
            # Executar cálculo
            calculadora.calcular_ganho_peso()
            calculadora.save()
            
            resultado = {
                'nome_cliente': calculadora.nome_cliente,
                'nome_fazenda': calculadora.nome_fazenda,
                'quantidade_animais': calculadora.quantidade_animais,
                'peso_inicial': calculadora.peso_inicial,
                'peso_final': calculadora.peso_final,
                'fator_ganho_peso': calculadora.fator_ganho_peso,
                'ganho_peso_unitario': (calculadora.peso_final - calculadora.peso_inicial) * calculadora.fator_ganho_peso,
                'resultado_final': calculadora.resultado_final,
                'proteina': calculadora.proteina,
                'energia': calculadora.energia,
                'fibra': calculadora.fibra,
                'carboidrato': calculadora.carboidrato,
                'gordura': calculadora.gordura,
            }
    
    context = {
        'form': form,
        'resultado': resultado,
    }
    return render(request, 'calculadoras/calculadora.html', context)
