from models import Join
from django import forms

# This is a regular form with added fields
class EmailForm(forms.Form):
	email = forms.EmailField()
	name = forms.CharField(required=False)

# This is a model fon\rm
class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ['email']