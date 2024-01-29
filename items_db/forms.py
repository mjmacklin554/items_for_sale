from django import forms
from django.forms import ModelForm
from .models import Item, Source


class ItemForm(ModelForm):

	#def __init__(self, *args, **kwargs):
		#super().__init__(*args, **kwargs)
		#self.fields['source'].empty_label = 'Source'

	source = forms.ModelChoiceField(label="", widget=forms.Select(attrs={'class': 'form-control'}),queryset=Source.objects.all(), empty_label="Placeholder")
		

	class Meta:		

		model = Item
		fields = ('item_name', 'category', 'description', 'source', 'value', 'sell', 'comments')
		labels = {
		'item_name': '',
		'category': '',
		'description': '',
		'source': '',
		'value': '',
		'sell': '',
		'comments': '',
		}
		
		widgets = {

		'item_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Item Name'}),
		'category': forms.TextInput(attrs={'class': 'form-control','placeholder':'Category'}),
		'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Description'}),
		'source': forms.Select(attrs={'class': 'form-control'}),
		'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Value'}),
		'sell': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Sell'}),
		'comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Comments'}),


		}
		