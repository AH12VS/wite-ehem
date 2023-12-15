from django import forms
from users.models import UserModel


class AccountForm(forms.Form):
    SEX_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    email = forms.CharField(
        label="E-Mail", widget=forms.EmailInput, required=True)
    fullname = forms.CharField(
        max_length="60", label="Full Name", required=False)
    passwd = forms.CharField(min_length="9", max_length="60",
                             label="Password", widget=forms.PasswordInput(), required=True)
    confrim_passwd = forms.CharField(
        min_length="9", max_length="60", label="Confrim Password", widget=forms.PasswordInput(), required=True)
    age = forms.IntegerField(label="Age", required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES,
                            label="Sex", widget=forms.RadioSelect)
    bio = forms.CharField(
        max_length="250", label=" Bio", widget=forms.TextInput, required=False)

    def clean(self):
        pass

    def clean_email(self):
        data = self.cleaned_data["email"]
        if not data:
            raise forms.ValidationError(
                "Email field must be in correct format")
        if UserModel.objects.filter(email=data).exists():
            raise forms.ValidationError(
                "An Account with the same email Bio is available")
        else:
            return data

    def clean_fullname(self):
        data = self.cleaned_data["fullname"]
        if len(data) > 60:
            raise forms.ValidationError(
                "Full Name length should be less than 61 character")
        else:
            return data

    def clean_passwd(self):
        data = self.cleaned_data["passwd"]
        if len(data) < 9 or len(data) > 60:
            raise forms.ValidationError(
                "Password length should be less than 61 character and greater than 8 character")
        else:
            return data

    def clean_confrim_passwd(self):
        passwd = self.cleaned_data["passwd"]
        confrim_passwd = self.cleaned_data["confrim_passwd"]
        if passwd != confrim_passwd:
            raise forms.ValidationError(
                "Confrim Password field should be same to Password field")
        else:
            return confrim_passwd

    def clean_age(self):
        data = self.cleaned_data["age"]
        try:
            data = int(data)
        except:
            if data == None:
                data = 1
            else:
                raise forms.ValidationError("Invalid Type for Age field")

        if data < 1 or data > 250:
            raise forms.ValidationError(
                "Age can not be less than 1 or greater than 250")

        return data

    def clean_sex(self):
        pass

    def clean_bio(self):
        data = self.cleaned_data["bio"]
        if len(data) > 1000:
            raise forms.ValidationError(
                "Bio length should be less than 250 character")
        else:
            return data


class ValidateAccountForm(forms.Form):
    code = forms.CharField(label="Code", max_length="6", required=True)
    passwd = forms.CharField(label="Password", min_length="9",
                             max_length="60", widget=forms.PasswordInput(), required=True)

    def clean_code(self):
        data = self.cleaned_data["code"]
        if len(data) < 6 or len(data) > 6:
            raise forms.ValidationError(
                "Verfication Code should be 6 digit and numerical")
        try:
            data = int(data)
        except:
            raise forms.ValidationError(
                "Verfication Code should be 6 digit and numerical")
        return data

    def clean_passwd(self):
        data = self.cleaned_data["passwd"]
        if len(data) < 9 or len(data) > 60:
            raise forms.ValidationError(
                "Password length should be less than 61 character and greater than 8 character")
        return data



# 
# from django import forms
# from users.models import UserModel
# from .ott import TOKENS
# 
# class AccountForm(forms.Form):
#     SEX_CHOICES = (
#         ("male", "Male"),
#         ("female", "Female"),
#         ("other", "Other"),
#     )
#     email = forms.CharField(
#         label="E-Mail", widget=forms.EmailInput, required=True)
#     fullname = forms.CharField(
#         max_length="60", label="Full Name", required=False)
#     passwd = forms.CharField(min_length="9", max_length="60",
#                              label="Password", widget=forms.PasswordInput(), required=True)
#     confrim_passwd = forms.CharField(
#         min_length="9", max_length="60", label="Confrim Password", widget=forms.PasswordInput(), required=True)
#     age = forms.IntegerField(label="Age", required=False)
#     sex = forms.ChoiceField(choices=SEX_CHOICES,
#                             label="Sex", widget=forms.RadioSelect)
#     bio = forms.CharField(
#         max_length="250", label=" Bio", widget=forms.TextInput, required=False)
# 
#     def clean(self):
#         pass
# 
#     def clean_email(self):
#         data = self.cleaned_data["email"]
#         if not data:
#             raise forms.ValidationError(
#                 "Email field must be in correct format")
#         if UserModel.objects.filter(email=data).exists():
#             raise forms.ValidationError(
#                 "An Account with the same email Bio is available")
#         else:
#             return data
# 
#     def clean_fullname(self):
#         data = self.cleaned_data["fullname"]
#         if len(data) > 60:
#             raise forms.ValidationError(
#                 "Full Name length should be less than 61 character")
#         else:
#             return data
# 
#     def clean_passwd(self):
#         data = self.cleaned_data["passwd"]
#         if len(data) < 9 or len(data) > 60:
#             raise forms.ValidationError(
#                 "Password length should be less than 61 character and greater than 8 character")
#         else:
#             return data
# 
#     def clean_confrim_passwd(self):
#         passwd = self.cleaned_data["passwd"]
#         confrim_passwd = self.cleaned_data["confrim_passwd"]
#         if passwd != confrim_passwd:
#             raise forms.ValidationError(
#                 "Confrim Password field should be same to Password field")
#         else:
#             return confrim_passwd
# 
#     def clean_age(self):
#         data = self.cleaned_data["age"]
#         try:
#             data = int(data)
#         except:
#             if data == None:
#                 data = 1
#             else:
#                 raise forms.ValidationError("Invalid Type for Age field")
# 
#         if data < 1 or data > 250:
#             raise forms.ValidationError(
#                 "Age can not be less than 1 or greater than 250")
# 
#         return data
# 
#     def clean_sex(self):
#         pass
# 
#     def clean_bio(self):
#         data = self.cleaned_data["bio"]
#         if len(data) > 1000:
#             raise forms.ValidationError(
#                 "Bio length should be less than 250 character")
#         else:
#             return data
# 
# 
# class ValidateAccountForm(forms.Form):
#     code = forms.CharField(label="Code", max_length="6", required=True)
#     passwd = forms.CharField(label="Password", min_length="9",
#                              max_length="60", widget=forms.PasswordInput(), required=True)
# 
#     def clean_code(self):
#         data = self.cleaned_data["code"]
#         if len(data) < 6 or len(data) > 6:
#             raise forms.ValidationError(
#                 "Verfication Code should be 6 digit and numerical")
#         try:
#             data = int(data)
#         except:
#             raise forms.ValidationError(
#                 "Verfication Code should be 6 digit and numerical")
#         if data not in TOKENS.values():
#             raise forms.ValidationError("Invalid TOKEN")
#         return data
# 
#     def clean_passwd(self):
#         data = self.cleaned_data["passwd"]
#         try:
#             code = self.cleaned_data["code"]
#         except:
#             raise forms.ValidationError("Invalid Token")
#         try:
#             user_pk = list(TOKENS.keys(list(TOKENS.values().index(code))))
#             user = UserModel.objects.get(id=int(user_pk))
#             if not user.check_password(data):
#                 raise forms.ValidationError("Wrong Password")
#         except:
#             raise forms.ValidationError("Invalid User")
#         if len(data) < 9 or len(data) > 60:
#             raise forms.ValidationError(
#                 "Password length should be less than 61 character and greater than 8 character")
        # return data
