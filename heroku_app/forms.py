from django import forms
from models import Join

# This regular form with added fields
class EmailForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()

# This model form
class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ['email'                                                                                       ]