from django import forms
from .models import zira

class ZiraForm(forms.ModelForm):
	class Meta:
		model = zira
		exclude = ('uploaded_by','date',)
