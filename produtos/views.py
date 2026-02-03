from django.shortcuts import render
from produtos.models import Produto
from django.views import View
from django.views.generic import DetailView

  
class ProdutosView(View):
  def get(self, request):
      produtos = Produto.objects.all().order_by('nome_produto')     
      search = request.GET.get('search')
      if search:
        produtos = produtos.filter(nome_produto__icontains=search)
      return render(
        request=request,
        template_name='produtos.html',
        context={'produtos': produtos},
      )
  
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'