from django import forms


from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {
                    "descripcion":"Descripción de la categoria",
                    "estado": "Estado"
                }
        widget = {"descripcion": forms.TextInput}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in item(self.fields):
            self.field[field].widget.attrs.update({
                'class': 'form-control'
            })