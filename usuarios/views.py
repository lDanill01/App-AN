import csv
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import ImportUsersForm
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods


@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class RegisterView(View):
    
    def get(self, request):
        user_form = UserCreationForm()
        import_form = ImportUsersForm()
        return render(
            request=request,
            template_name='register.html',
            context={'user_form': user_form, 'import_form': import_form},
        )
    
    def post(self, request):
        user_form = UserCreationForm()
        import_form = ImportUsersForm()
        
        # Importação: formulário com arquivo enviado
        if request.FILES.get('arquivo'):
            import_form = ImportUsersForm(request.POST, request.FILES)
            if import_form.is_valid():
                self._process_csv_import(request, request.FILES['arquivo'])
            import_form = ImportUsersForm()
        
        # Cadastro de um usuário
        else:
            user_form = UserCreationForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Usuário cadastrado com sucesso.')
                return redirect('login')
        
        return render(
            request=request,
            template_name='register.html',
            context={'user_form': user_form, 'import_form': import_form},
        )
    
    def _process_csv_import(self, request, arquivo):
        """Processa importação de usuários via CSV."""
        if not arquivo.name.endswith('.csv'):
            messages.error(request, 'Envie apenas arquivos com extensão .csv')
            return
        
        try:
            conteudo = arquivo.read().decode('utf-8-sig')
        except UnicodeDecodeError:
            messages.error(request, 'O arquivo deve estar em UTF-8.')
            return
        
        linhas = csv.DictReader(conteudo.splitlines())
        criados = []
        colunas_obrigatorias = {'username', 'password'}
        
        for num, linha in enumerate(linhas, start=2):
            linha = {k.strip().lower(): (v.strip() if v else '') for k, v in linha.items()}
            
            if not linha.get('username') and not linha.get('password'):
                continue
            
            if not colunas_obrigatorias.issubset(linha.keys()):
                messages.warning(
                    request,
                    f'Linha {num}: faltam colunas. Use: username, password (e opcional: email, first_name, last_name).',
                )
                continue
            
            username = linha.get('username', '').strip()
            password = linha.get('password', '').strip()
            
            if not username or not password:
                messages.warning(request, f'Linha {num}: username e password são obrigatórios.')
                continue
            
            try:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, f'Linha {num}: usuário "{username}" já existe.')
                    continue
                
                User.objects.create_user(
                    username=username,
                    password=password,
                    email=linha.get('email', '').strip() or '',
                    first_name=linha.get('first_name', '').strip(),
                    last_name=linha.get('last_name', '').strip(),
                )
                criados.append(username)
            except Exception as e:
                messages.warning(request, f'Linha {num} ({username}): {str(e)}')
        
        if criados:
            messages.success(request, f'{len(criados)} usuário(s) criado(s): {", ".join(criados)}.')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('novo_produto')
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='login.html',
        context={'form': form},
    )

def logout_view(request):
    logout(request)
    return redirect('novo_produto')