from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
from .models import Produto, Marca, Especie, Divisao, Linha
import csv
import io


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    list_editable = ('ativo',)
    
    change_list_template = "produtos/marca_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-csv/', self.importar_csv, name='marca_importar_csv'),
        ]
        return custom_urls + urls

    def importar_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            
            if not csv_file or not csv_file.name.endswith('.csv'):
                messages.error(request, "Por favor, envie um arquivo CSV válido.")
                return redirect("..")

            try:
                decoded_file = csv_file.read().decode('utf-8-sig')
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)
                
                criados = 0
                atualizados = 0
                
                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue
                    
                    descricao = row.get('descricao', '').strip()
                    ativo = row.get('ativo', 'True').strip().lower() in ['true', '1', 'sim', 'yes']
                    
                    marca, created = Marca.objects.update_or_create(
                        nome=nome,
                        defaults={'descricao': descricao, 'ativo': ativo}
                    )
                    
                    if created:
                        criados += 1
                    else:
                        atualizados += 1
                
                messages.success(
                    request,
                    f"Importação concluída! {criados} marcas criadas, {atualizados} atualizadas."
                )
                
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
            
            return redirect("..")
        
        context = {
            'title': 'Importar Marcas via CSV',
            'colunas': 'nome, descricao, ativo',
            'exemplo': 'Nike,Marca esportiva,True\nAdidas,Marca alemã,True'
        }
        return render(request, "admin/csv_form.html", context)


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    list_editable = ('ativo',)
    
    change_list_template = "produtos/especie_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-csv/', self.importar_csv, name='especie_importar_csv'),
        ]
        return custom_urls + urls

    def importar_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            
            if not csv_file or not csv_file.name.endswith('.csv'):
                messages.error(request, "Por favor, envie um arquivo CSV válido.")
                return redirect("..")

            try:
                decoded_file = csv_file.read().decode('utf-8-sig')
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)
                
                criados = 0
                atualizados = 0
                
                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue
                    
                    descricao = row.get('descricao', '').strip()
                    ativo = row.get('ativo', 'True').strip().lower() in ['true', '1', 'sim', 'yes']
                    
                    especie, created = Especie.objects.update_or_create(
                        nome=nome,
                        defaults={'descricao': descricao, 'ativo': ativo}
                    )
                    
                    if created:
                        criados += 1
                    else:
                        atualizados += 1
                
                messages.success(
                    request,
                    f"Importação concluída! {criados} espécies criadas, {atualizados} atualizadas."
                )
                
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
            
            return redirect("..")
        
        context = {
            'title': 'Importar Espécies via CSV',
            'colunas': 'nome, descricao, ativo',
            'exemplo': 'Tênis,Calçado esportivo,True\nCamiseta,Vestuário,True'
        }
        return render(request, "admin/csv_form.html", context)


@admin.register(Divisao)
class DivisaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    list_editable = ('ativo',)
    
    change_list_template = "produtos/divisao_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-csv/', self.importar_csv, name='divisao_importar_csv'),
        ]
        return custom_urls + urls

    def importar_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            
            if not csv_file or not csv_file.name.endswith('.csv'):
                messages.error(request, "Por favor, envie um arquivo CSV válido.")
                return redirect("..")

            try:
                decoded_file = csv_file.read().decode('utf-8-sig')
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)
                
                criados = 0
                atualizados = 0
                
                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue
                    
                    descricao = row.get('descricao', '').strip()
                    ativo = row.get('ativo', 'True').strip().lower() in ['true', '1', 'sim', 'yes']
                    
                    divisao, created = Divisao.objects.update_or_create(
                        nome=nome,
                        defaults={'descricao': descricao, 'ativo': ativo}
                    )
                    
                    if created:
                        criados += 1
                    else:
                        atualizados += 1
                
                messages.success(
                    request,
                    f"Importação concluída! {criados} divisões criadas, {atualizados} atualizadas."
                )
                
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
            
            return redirect("..")
        
        context = {
            'title': 'Importar Divisões via CSV',
            'colunas': 'nome, descricao, ativo',
            'exemplo': 'Masculino,Produtos masculinos,True\nFeminino,Produtos femininos,True'
        }
        return render(request, "admin/csv_form.html", context)


@admin.register(Linha)
class LinhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    list_editable = ('ativo',)
    
    change_list_template = "produtos/linha_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-csv/', self.importar_csv, name='linha_importar_csv'),
        ]
        return custom_urls + urls

    def importar_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            
            if not csv_file or not csv_file.name.endswith('.csv'):
                messages.error(request, "Por favor, envie um arquivo CSV válido.")
                return redirect("..")

            try:
                decoded_file = csv_file.read().decode('utf-8-sig')
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)
                
                criados = 0
                atualizados = 0
                
                for row in reader:
                    nome = row.get('nome', '').strip()
                    if not nome:
                        continue
                    
                    descricao = row.get('descricao', '').strip()
                    ativo = row.get('ativo', 'True').strip().lower() in ['true', '1', 'sim', 'yes']
                    
                    linha, created = Linha.objects.update_or_create(
                        nome=nome,
                        defaults={'descricao': descricao, 'ativo': ativo}
                    )
                    
                    if created:
                        criados += 1
                    else:
                        atualizados += 1
                
                messages.success(
                    request,
                    f"Importação concluída! {criados} linhas criadas, {atualizados} atualizadas."
                )
                
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
            
            return redirect("..")
        
        context = {
            'title': 'Importar Linhas via CSV',
            'colunas': 'nome, descricao, ativo',
            'exemplo': 'Premium,Linha premium,True\nEssential,Linha essencial,True'
        }
        return render(request, "admin/csv_form.html", context)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'marca', 'especie', 'divisao', 'linha', 'ativo')
    list_filter = ('ativo', 'marca', 'especie', 'divisao', 'linha')
    search_fields = ('nome_produto', 'marca__nome')
    list_editable = ('ativo',)
    
    change_list_template = "produtos/produtos_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-csv/', self.importar_csv, name='produtos_importar_csv'),
        ]
        return custom_urls + urls

    def importar_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES.get("csv_file")
            
            if not csv_file or not csv_file.name.endswith('.csv'):
                messages.error(request, "Por favor, envie um arquivo CSV válido.")
                return redirect("..")

            try:
                decoded_file = csv_file.read().decode('utf-8-sig')
                io_string = io.StringIO(decoded_file)
                reader = csv.DictReader(io_string)
                
                criados = 0
                atualizados = 0
                erros = []
                
                for linha_num, row in enumerate(reader, start=2):
                    nome_produto = row.get('nome_produto', '').strip()
                    marca_nome = row.get('marca', '').strip()
                    especie_nome = row.get('especie', '').strip()
                    divisao_nome = row.get('divisao', '').strip()
                    linha_nome = row.get('linha', '').strip()
                    
                    if not nome_produto:
                        erros.append(f"Linha {linha_num}: nome_produto é obrigatório")
                        continue
                    
                    try:
                        marca = Marca.objects.get(nome=marca_nome)
                        especie = Especie.objects.get(nome=especie_nome)
                        divisao = Divisao.objects.get(nome=divisao_nome)
                        linha = Linha.objects.get(nome=linha_nome)
                    except Marca.DoesNotExist:
                        erros.append(f"Linha {linha_num}: Marca '{marca_nome}' não encontrada")
                        continue
                    except Especie.DoesNotExist:
                        erros.append(f"Linha {linha_num}: Espécie '{especie_nome}' não encontrada")
                        continue
                    except Divisao.DoesNotExist:
                        erros.append(f"Linha {linha_num}: Divisão '{divisao_nome}' não encontrada")
                        continue
                    except Linha.DoesNotExist:
                        erros.append(f"Linha {linha_num}: Linha '{linha_nome}' não encontrada")
                        continue
                    
                    ativo = row.get('ativo', 'True').strip().lower() in ['true', '1', 'sim', 'yes']
                    
                    produto, created = Produto.objects.update_or_create(
                        nome_produto=nome_produto,
                        marca=marca,
                        defaults={
                            'especie': especie,
                            'divisao': divisao,
                            'linha': linha,
                            'ativo': ativo,
                        }
                    )
                    
                    if created:
                        criados += 1
                    else:
                        atualizados += 1
                
                if erros:
                    messages.warning(request, "Alguns registros não foram importados:\n" + "\n".join(erros))
                
                if criados or atualizados:
                    messages.success(
                        request,
                        f"Importação concluída! {criados} produtos criados, {atualizados} atualizados."
                    )
                
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
            
            return redirect("..")
        
        context = {
            'title': 'Importar Produtos via CSV',
            'colunas': 'nome_produto, marca, especie, divisao, linha, ativo',
            'exemplo': 'Air Max 90,Nike,Tênis,Masculino,Premium,True\nUltraboost,Adidas,Tênis,Feminino,Essential,True',
            'observacao': 'IMPORTANTE: Antes de importar produtos, certifique-se de que as Marcas, Espécies, Divisões e Linhas já estão cadastradas!'
        }
        return render(request, "admin/csv_form.html", context)