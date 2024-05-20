from django import forms


class TemperatureConverterForm(forms.Form):
    CHOICES = [
        {'c_to_f', 'Celsius to Fahrenheit'},
        {'f_to_c', 'Fahrenheit to Celsius'},
        {'c_to_k', 'Celsius to Kelvin'},
        {'k_to_c', 'Kelvin to Celsius'},
        {'f_to_k', 'Fahrenheit to Kelvin'},
        {'k_to_f', 'Kelvin to Fahrenheit'},
    ]

    temperature = forms.FloatField(label='Input Temperature')
    conversion_type = forms.ChoiceField(choices=CHOICES, label='Conversion Type')
