from django.shortcuts import render
from produtos.models import Produto
from django.views import View

  
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