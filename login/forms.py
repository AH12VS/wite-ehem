# from django import forms
# from users.models import UserModel


# class LoginForm(forms.Form):
#     email = forms.CharField(
#         label="E-Mail", widget=forms.EmailInput, required=True)
#     passwd = forms.CharField(min_length="6", max_length="60",
#                              label="Password", widget=forms.PasswordInput(), required=True)

#     def clean(self):
#         pass

#     def clean_email(self):
#         data = self.cleaned_data["email"]
#         if not data:
#             raise forms.ValidationError(
#                 "Email field must be in correct format")
#         if UserModel.objects.filter(email=data).exists():
#             return data
#         else:
#             raise forms.ValidationError(
#                 "There is no account with this datas")

#     def clean_passwd(self):
#         data = self.cleaned_data["passwd"]
#         if len(data) < 9 or len(data) > 60:
#             raise forms.ValidationError(
#                 "Password length should be less than 61 character and greater than 8 character")
#         else:
#             return data


from django import forms
from users.models import UserModel


class LoginForm(forms.Form):
    email = forms.CharField(
        label="E-Mail", widget=forms.EmailInput, required=True)
    passwd = forms.CharField(min_length="6", max_length="60",
                             label="Password", widget=forms.PasswordInput(), required=True)

    def clean(self):
        pass

    def clean_email(self):
        data = self.cleaned_data["email"]
        if not data:
            raise forms.ValidationError(
                "Email field must be in correct format")
        if UserModel.objects.filter(email=data).exists():
            return data
        else:
            raise forms.ValidationError(
                "There is no account with this datas")

    def clean_passwd(self):
        data = self.cleaned_data["passwd"]
        try:
            user = UserModel.objects.get(email__exact=self.cleaned_data["email"])
        except:
            raise forms.ValidationError("Can not find a user with this email")
        
        if len(data) < 9 or len(data) > 60:
            raise forms.ValidationError(
                "Password length should be less than 61 character and greater than 8 character") 
        if not user.check_password(data):
            raise forms.ValidationError("Invalid Password for this Account")

        return data


