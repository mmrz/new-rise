from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Comment, Product


class CommentForm(forms.Form):
    cm_text = forms.CharField(label='comment', max_length=500, required=False)

