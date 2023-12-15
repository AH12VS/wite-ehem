from django import forms


class ContactusForm(forms.Form):
    SUBJECT_CHOICES = (
        ("other", "Other"),
        ("critics", "Critics"),
        ("suggestion", "Suggestion"),
    )
    fullname = forms.CharField(
        max_length="60", label="Full Name", required=True)
    email = forms.CharField(
        label="E-Mail", widget=forms.EmailInput(), required=True)
    subject = forms.ChoiceField(
        label="Subject", choices=SUBJECT_CHOICES, required=True)
    message = forms.CharField(
        max_length="1000", label="Message", widget=forms.TextInput(), required=True)

    def clean(self):
        pass

    def clean_fullname(self):
        data = self.cleaned_data["fullname"]
        if len(data) > 60:
            raise forms.ValidationError(
                "Full Name length should be less than 61 character")
        else:
            return data

    def clean_email(self):
        data = self.cleaned_data["email"]
        if not data:
            raise forms.ValidationError(
                "Email field must be in correct format")
        else:
            return data

    def clean_subject(self):
        data = self.cleaned_data["subject"]
        if not data:
            raise forms.ValidationError("Invalid subject")
        return data

    def clean_message(self):
        data = self.cleaned_data["message"]
        if len(data) > 1000:
            raise forms.ValidationError(
                "Message length should be less than 1001 characters")
        return data
