from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellidos", "nacionalidad", "descripcion"]
        labels = {
            "nombre": "Nombre del autor",
            "apellidos": "Apellidos del autor",
            "nacionalidad": "Nacionalidad del autor",
            "descripcion": "breve descripcion del autor",
        }

    def __init__(self, *a, **k):
        """
        todo esto unicamente para que todos los campos a rellenar tengan esa clase de boostrap...
        no se deberia hacer esto aca, pero bueno.
        """
        super(AutorForm, self).__init__(*a, **k)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
