from django import forms
from ProfileApp.models import *

series_choice = [('Series i', 'Series i'),
                 ('Series X', 'Series X'),
                 ('Series M', 'Series M'),
                 ('Series 7', 'Series 7'),
                 ('Series Concept Cars', 'Series Concept Cars'),
                 ('Brochure', 'Brochure')]

bodyTypes_Choice = [('Coupe', 'Coupe'),
                    ('Convertible', 'Convertible'),
                    ('Sedan', 'Sedan'),
                    ('Sport Activity Coupe', 'Sport Activity Coupe'),
                    ('Sport Activity Vehicle', 'Sport Activity Vehicle'),
                    ('Roadster', 'Roadster'),
                    ('Gran Coupe', 'Gran Coupe'),
                    ('Gran Turismo', 'Gran Turismo')]

system_Choice = [('Full-Electrlc', 'Full-Electrlc'),
              ('Diesel', 'Diesel'),
              ('Gasoline', 'Gasoline'),
              ('Plug-In Hybri', 'Plug-In Hybri')]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','series', 'bodyTypes', 'color', 'system', 'net')
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'series': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=series_choice),
            'bodyTypes': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=bodyTypes_Choice),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'system': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=system_Choice),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'id': 'ID',
            'series': 'Series',
            'bodyTypes': 'BodyTypes',
            'color': 'Color',
            'system': 'System',
            'net': 'Net',
        }