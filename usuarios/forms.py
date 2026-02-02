
from django import forms


class ImportUsersForm(forms.Form):
    """Formulário para upload de arquivo CSV com lista de usuários."""

    arquivo = forms.FileField(
        label='Arquivo CSV',
        help_text='Arquivo com colunas: username, email, password, first_name, last_name',
        widget=forms.FileInput(attrs={'accept': '.csv'}),
    )
