from django import forms

from matery.models import matery

class FormMatery(forms.ModelForm):

	class Meta:
		model = matery

		fields = [
			'user',
			'Nombre',
			'Orientacion1',
			'Orientacion2',
			'Orientacion3',
			'Orientacion4',
			'Orientacion5',
			
		]
		labels = {
			'user': 'Seleccione su usuario',
			'Nombre': 'Nombre de la materia',
			'Orientacion1': '¿Que son los números naturales?',
			'Orientacion2': '¿Que son los números enteros?',
			'Orientacion3': '√432',
			'Orientacion4': '2918838/897',
			'Orientacion5': '(45/26)*(39/25)*(22/33)',
			
		}
		widgets = {
			'Nombbre': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion1': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion2': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion3': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion4': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion5': forms.TextInput(attrs={'class':'form-control'}),
		}
