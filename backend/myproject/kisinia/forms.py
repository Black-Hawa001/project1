from django import forms
from .models import vyakula

class FoodForm (forms.ModelForm):
	class Meta:
		model = vyakula
		fields = [
		'name',
		'category',
		'description',
		'address',
		]