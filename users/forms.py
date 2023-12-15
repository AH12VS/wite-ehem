from django import forms


class UserDetailEditForm(forms.Form):
    SEX_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    fullname = forms.CharField(
        max_length="60", label="Full Name", required=False)
    age = forms.IntegerField(label="Age", required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES,
                            label="Sex", widget=forms.RadioSelect)
    bio = forms.CharField(
        max_length="250", label=" Bio", widget=forms.TextInput, required=False)
    image_prof = forms.ImageField(label="Image", required=False)

    def clean(self):
        pass

    def clean_fullname(self):
        data = self.cleaned_data["fullname"]
        if len(data) > 60:
            raise forms.ValidationError(
                "Full Name length should be less than 61 character")
        else:
            return data

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


class UserChangePasswdForm(forms.Form):
    old_passwd = forms.CharField(min_length="9", max_length="60",
                                 label="Old Password", widget=forms.PasswordInput(), required=True)
    new_passwd = forms.CharField(min_length="9", max_length="60",
                                 label="New Password", widget=forms.PasswordInput(), required=True)
    confrim_new_passwd = forms.CharField(min_length="9", max_length="60",
                                         label="Confrim New Password", widget=forms.PasswordInput(), required=True)

    def clean_old_passwd(self):
        data = self.cleaned_data["old_passwd"]
        if len(data) < 9 or len(data) > 60:
            raise forms.ValidationError(
                "Password length should be less than 61 character and greater than 8 character")
        return data

    def clean_new_passwd(self):
        data = self.cleaned_data["new_passwd"]
        if len(data) < 9 or len(data) > 60:
            raise forms.ValidationError(
                "Password length should be less than 61 character and greater than 8 character")
        return data

    def clean_confrim_new_passwd(self):
        new_passwd = self.cleaned_data["new_passwd"]
        confrim_new_passwd = self.cleaned_data["confrim_new_passwd"]
        if new_passwd != confrim_new_passwd:
            raise forms.ValidationError(
                "Confrim New Password field should be same to New Password field")
        return confrim_new_passwd
