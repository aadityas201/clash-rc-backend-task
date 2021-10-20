from django import forms
from django.forms.widgets import Widget

choices = [
    ('1','Extract numbers from a string greater than 100'),
    ('2','Extract date from the url string'),
    ('3','Extract strings within Single qoute'),
    ('4','Email Validator'),
    ('5','Validate Ip address and determine class'),
    ('6','Validate MAC address'),
    ('7','Convert camelCase to snake_case')
]
class optionForm(forms.Form):
    Input=forms.CharField()
    options= forms.CharField(label='Select any one of the following', widget=forms.RadioSelect(choices=choices))
