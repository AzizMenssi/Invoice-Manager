from django import forms
from main.models import CompteBancaire


class CompteBancaireForm(forms.Form):
    IdCB = forms.CharField(max_length=100)
    NumB = forms.CharField(max_length=100)
    CodeS=forms.CharField(max_length=100)
    AdresseB_fr = forms.CharField(max_length=100)
    AdresseB_an = forms.CharField(max_length=100)
    AdresseB_ar = forms.CharField(max_length=100)

    class Meta:
        model =CompteBancaire
        fields =('NumB','CodeS')
