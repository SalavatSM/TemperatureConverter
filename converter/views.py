from django.shortcuts import render
from .forms import TemperatureConverterForm


def converter_temperature(temp, conversion_type):
    if conversion_type == 'c_to_f':
        return (temp * 9/5) + 32
    elif conversion_type == 'f_to_c':
        return (temp - 32) * 5/9
    elif conversion_type == 'c_to_k':
        return (temp + 273)
    elif conversion_type == 'k_to_c':
        return (temp - 273)
    elif conversion_type == 'f_to_k':
        return (temp - 32) * 5/9 + 273
    elif conversion_type == 'k_to_f':
        return (temp - 273) * 9/5 + 32


def index(request):
    result = None
    if request.method == 'POST':
        form = TemperatureConverterForm(request.POST)
        if form.is_valid():
            temp = form.cleaned_data['temperature']
            conversion_type = form.cleaned_data['conversion_type']
            result = converter_temperature(temp, conversion_type)
    else:
        form = TemperatureConverterForm()
    return render(request, 'index.html', {'form': form, 'result': result})