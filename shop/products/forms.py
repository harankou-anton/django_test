from django import forms

COLOR_CHOISES = (
    ('RED', 'Red'),
    ('BLUE', 'Blue'),
    ('GREEN', 'Green')
)


class ProductAdd(forms.Form):
    title = forms.CharField(max_length=255)
    price = forms.IntegerField(min_value=0)
    description = forms.CharField(max_length=255, required=False)
    color = forms.ChoiceField(choices=COLOR_CHOISES)
