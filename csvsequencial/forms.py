from django import forms

class Gerador_csv(forms.Form):
    codigo_base = forms.CharField(
        label='Código Base',
        max_length=25,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ex: EVENTO-SP'}
        ),
    )
    
    caminho = forms.CharField(
        label='Caminho',
        max_length=80,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': r'Ex: C:\Documentos\adesivosArbo\marilandiadosul\qrCodes'}
        ),
    )
    
    quantidadeInicial = forms.IntegerField(
        label='Quantidade Inicial',
        min_value=1,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Ex: 50'}
        ),
    )

    quantidadeFinal = forms.IntegerField(
        label='Quantidade Final',
        min_value=1,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Ex: 100'}
        ),
    )

    def clean(self):
        cleaned_data = super().clean()

        quantidade_inicial = cleaned_data.get("quantidadeInicial")
        quantidade_final = cleaned_data.get("quantidadeFinal")

        if quantidade_inicial and quantidade_final:
            if quantidade_final < quantidade_inicial:
                raise forms.ValidationError(
                    "A Quantidade Final não pode ser menor que a Quantidade Inicial."
                )

        return cleaned_data