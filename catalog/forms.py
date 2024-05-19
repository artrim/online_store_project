from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name_product', 'description_product', 'picture', 'price',)

    def clean_name_product(self):
        cleaned_data = self.cleaned_data['name_product']
        bad_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for i in bad_list:
            if i in cleaned_data:
                raise forms.ValidationError(f'В наименовании содержится запрещенное слово "{i}"')

        return cleaned_data

    def clean_description_product(self):
        cleaned_data = self.cleaned_data['description_product']
        bad_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for i in bad_list:
            if i in cleaned_data:
                raise forms.ValidationError(f'В описании содержится запрещенное слово "{i}"')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
