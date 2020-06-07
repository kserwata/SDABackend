from django import forms
from .models import Car
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class SimpleCarForm(forms.Form):
    brand = forms.CharField(max_length=30)
    model = forms.CharField(max_length=30)


class ModelCarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelCarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('brand', css_class='form-group col-md-6 mb-0'),
                Column('model', css_class='form-group col-md-6 mb-0'),
                css_class='form-row text-center'
            ),
            Row(
                Column('petrol', css_class='form-group col-md-4 mb-0'),
                Column('year', css_class='form-group col-md-4 mb-0'),
                Column('doors', css_class='form-group col-md-4 mb-0')
            ),
            Submit('submit', 'Zapisz', css_class='col-md-12')
        )

    class Meta:
        model = Car
        fields = '__all__'