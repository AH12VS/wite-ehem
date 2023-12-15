from django import forms
# from .models import CommentModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget 


class CommentForm(forms.Form):
    name = forms.CharField(max_length="60", label="Name", required=True)
    comment = forms.CharField(label="Comment", widget=forms.TextInput())

    def clean(self):
        pass

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) > 60:
            raise forms.ValidationError(
                "Name length should be less than 61 character")
        return data

    def clean_comment(self):
        data = self.cleaned_data["comment"]
        if len(data) > 1000:
            raise forms.ValidationError(
                "Comment length should be less than 1001 character")
        return data


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=60, label="Title", required=True)
    # body = forms.CharField(
    #     label="Body", widget=forms.TextInput(), required=True)
    body = forms.CharField(
        label="Body", widget=CKEditorUploadingWidget(), required=True)
    thumbnail = forms.ImageField(label="Post Thumbnail", required=False)
    tags = forms.CharField(label="Tags", required=False)


    def clean(self):
        pass

    def clean_title(self):
        data = self.cleaned_data["title"]
        if not data:
            raise forms.ValidationError("Title field can not be empty")
        return data

    def clean_body(self):
        data = self.cleaned_data["body"]
        if not data:
            raise forms.ValidationError("Body field can not be empty")
        return data

