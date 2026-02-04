from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Produto.objects.filter(ativo=True).select_related(
            'marca', 'especie', 'divisao', 'linha'
        )
        
        # Filtros opcionais
        marca = self.request.GET.get('marca')
        especie = self.request.GET.get('especie')
        divisao = self.request.GET.get('divisao')
        linha = self.request.GET.get('linha')
        busca = self.request.GET.get('q')
        
        if marca:
            queryset = queryset.filter(marca_id=marca)
        if especie:
            queryset = queryset.filter(especie_id=especie)
        if divisao:
            queryset = queryset.filter(divisao_id=divisao)
        if linha:
            queryset = queryset.filter(linha_id=linha)
        if busca:
            queryset = queryset.filter(nome_produto__icontains=busca)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicionar dados para filtros
        from .models import Marca, Especie, Divisao, Linha
        context['marcas'] = Marca.objects.filter(ativo=True)
        context['especies'] = Especie.objects.filter(ativo=True)
        context['divisoes'] = Divisao.objects.filter(ativo=True)
        context['linhas'] = Linha.objects.filter(ativo=True)
        return context


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'
    
    def get_queryset(self):
        return Produto.objects.filter(ativo=True).select_related(
            'marca', 'especie', 'divisao', 'linha'
        )