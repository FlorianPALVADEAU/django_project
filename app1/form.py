from django import forms
from .models import Image


# creating a form
class createForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Image

		# specify fields to be used
		fields = [
			"name",
			"url",
			"stock",
			"prix",
		]
