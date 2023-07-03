from django import forms
from .models import OPD_Reg

class OPD_Reg_form(forms.ModelForm):
    class Meta:
        model=OPD_Reg
        fields="__all__"
        CHOICES = [('0','SELECT GENDER'),('MALE', 'MALE'), ('FEMALE', 'FEMALE'),('OTHER','OTHER')]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name Here'}),
            'dob':  forms.NumberInput(attrs={'type':'date','placeholder': 'BirthDate'}),
            'gender':forms.Select(choices=CHOICES),
            'addr':forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'Enter Your Address'}),
            'ph_no':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile Number Here'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email ID Here'}),


        }







    # address1 = models.CharField(
    #     "Address line 1",
    #     max_length=1024,
    # )
    #
    # address2 = models.CharField(
    #     "Address line 2",
    #     max_length=1024,
    # )
    #
    # zip_code = models.CharField(
    #     "ZIP / Postal code",
    #     max_length=12,
    # )
    #
    # city = models.CharField(
    #     "City",
    #     max_length=1024,
    # )
    #
    # country = models.CharField(
    #     "Country",
    #     max_length=3,
    #
    # )
# rom django.forms.widgets import NumberInput
# class SampleForm(forms.Form):
#     name = forms.CharField()
#     date_of_birth = forms.DateField(widget = NumberInput(attrs={'type':'date'}))
# class PictureForm(forms.Form):
#     CHOICES = [
#         ('1', 'Option 1'),
#         ('2', 'Option 2'),
#     ]
#     like = forms.ChoiceField(
#         widget=forms.RadioSelect,
#         choices=CHOICES,
#     )
# Date = forms.DateField(widget = forms.SelectDateWidget)
# forms.widgets.DateInput
# # class DateForm(forms.Form):
# #     date = forms.DateTimeField(
# #         input_formats=['%d/%m/%Y %H:%M'],
# #         widget=forms.DateTimeInput(attrs={
# #             'class': 'form-control datetimepicker-input',
# #             'data-target': '#datetimepicker1'
# #         })
#     )