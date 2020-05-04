from django import forms
from .models import Comment
from mysite.settings import EMAIL_HOST_USER

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('text', 'created_on')


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

