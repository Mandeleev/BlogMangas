from .models import Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

class SomeForm(forms.Form):
	foo = forms.CharField(widget = SummernoteWidget())