from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import messages
import csv
import io


class UserAdmin(BaseUserAdmin):
    change_list_template = "usuarios/user_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('importar-csv/', self.importar_csv, name='user_importar_csv'),
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
                    username = row.get('username', '').strip()
                    email = row.get('email', '').strip()
                    first_name = row.get('first_name', '').strip()
                    last_name = row.get('last_name', '').strip()
                    password = row.get('password', '').strip()
                    is_staff = row.get('is_staff', 'False').strip().lower() in ['true', '1', 'sim', 'yes']
                    is_superuser = row.get('is_superuser', 'False').strip().lower() in ['true', '1', 'sim', 'yes']
                    is_active = row.get('is_active', 'True').strip().lower() in ['true', '1', 'sim', 'yes']
                    
                    if not username:
                        erros.append(f"Linha {linha_num}: username é obrigatório")
                        continue
                    
                    # Verificar se o usuário já existe
                    user, created = User.objects.get_or_create(
                        username=username,
                        defaults={
                            'email': email,
                            'first_name': first_name,
                            'last_name': last_name,
                            'is_staff': is_staff,
                            'is_superuser': is_superuser,
                            'is_active': is_active,
                        }
                    )
                    
                    # Se já existir, atualizar os dados
                    if not created:
                        user.email = email
                        user.first_name = first_name
                        user.last_name = last_name
                        user.is_staff = is_staff
                        user.is_superuser = is_superuser
                        user.is_active = is_active
                    
                    # Definir senha (apenas se fornecida)
                    if password:
                        user.set_password(password)
                    elif created:
                        # Se é um novo usuário e não tem senha, define uma padrão
                        user.set_password('senha123')
                        erros.append(f"Linha {linha_num}: Usuário '{username}' criado com senha padrão 'senha123'")
                    
                    user.save()
                    
                    if created:
                        criados += 1
                    else:
                        atualizados += 1
                
                if erros:
                    messages.warning(request, "Avisos:\n" + "\n".join(erros))
                
                if criados or atualizados:
                    messages.success(
                        request,
                        f"Importação concluída! {criados} usuários criados, {atualizados} atualizados."
                    )
                
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {str(e)}")
            
            return redirect("..")
        
        context = {
            'title': 'Importar Usuários via CSV',
            'colunas': 'username, email, first_name, last_name, password, is_staff, is_superuser, is_active',
            'exemplo': 'joao.silva,joao@email.com,João,Silva,senha123,False,False,True\nmaria.santos,maria@email.com,Maria,Santos,senha456,True,False,True',
            'observacao': 'IMPORTANTE: Esta funcionalidade está disponível apenas para superusuários. Senhas são armazenadas de forma segura (hash).'
        }
        return render(request, "admin/csv_form.html", context)


# Desregistrar o UserAdmin padrão e registrar o customizado
admin.site.unregister(User)
admin.site.register(User, UserAdmin)