from django import forms
from .models import TarefaModel


class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['nome', 'descricao', 'prazo', 'completo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'completo':
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control', 'placeholder': f'Insira {field.label.lower()}'})
