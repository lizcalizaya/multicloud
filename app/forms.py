from django import forms
from .models import ArchivoMulticloud


class ArchivoMulticloudForm(forms.ModelForm):
    class Meta:
        model = ArchivoMulticloud
        fields = ['titulo', 'descripcion', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ej. Evidencia de seguridad',
                'maxlength': '100'
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Descripción breve del archivo',
                'rows': 3
            }),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if len(titulo) < 3:
            raise forms.ValidationError('El título debe tener al menos 3 caracteres.')
        return titulo

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')

        if archivo:
            limite_mb = 5
            if archivo.size > limite_mb * 1024 * 1024:
                raise forms.ValidationError('El archivo no puede superar los 5 MB.')

        return archivo