from django import forms

class AssetForm(forms.Form):

    AssetThumbnail = forms.ImageField(label = '', required=False)

    subjectArea = forms.CharField(max_length=30, label = '', required=False, widget=forms.TextInput(attrs={'placeholder': 'Subject Area', 'style': 'width: 300px;', 'class': 'form-control'}))

    assetLocation = forms.CharField(max_length=30, label = '', required=False, widget=forms.TextInput(attrs={'placeholder': 'Current Location', 'style': 'width: 300px;', 'class': 'form-control'}))
