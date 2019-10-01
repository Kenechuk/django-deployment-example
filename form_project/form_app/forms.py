from django import forms
from django.core import validators

def check_er(z):
    if z[0].lower() != 'k':
        raise forms.ValidationError("Make Sure it starts with z")


class FormName(forms.Form):
    name = forms.CharField()
    # email = forms.EmailField(validators=[check_er])
    email = forms.EmailField(validators=[check_er])
    verify_email = forms.EmailField(label="Please enter your mail again: ")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_neat = super().clean()
        email = all_neat['email']
        vemail = all_neat['verify_email']
        if email != vemail:
            raise forms.ValidationError("Please Check Your Email")


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Got Bot")
    #     return botcatcher
