from inputforms.models import *
from django import forms
from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class AccdForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-accident-details-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Record', css_class='btn btn-success pull-right'))
        super(AccdForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(AccdForm, self).clean()
        accd_type = cleaned_data.get("accd_type")
        if accd_type == 'Fatal':
            LP = cleaned_data.get("learning_point")
            if LP == '':
                msg = forms.ValidationError("This field is required.")
                self.add_error('learning_point', msg)
        else:
            cleaned_data['learning_point'] = '----'
        return cleaned_data

    class Meta:
        model = AllAccident
        exclude = ["unit_name", ]
        help_texts = {
            'date': ('Date Format: YYYY-MM-DD, Time Format: HH:MM, Example: 2017-12-12 15:30'),
        }


class ManhoursForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'id-manhours-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Record', css_class='btn btn-success pull-right'))
        self.helper.layout = Layout(
            Field('date', id="manhours_date"),
            Field('manhours_worked_regular',),
            Field('manhours_worked_contract',),
            Field('mandays_lost',),
        )
        super(ManhoursForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Manhours
        exclude = ["unit_name", ]
