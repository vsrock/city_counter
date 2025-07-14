from django.shortcuts import render
from .forms import LetterForm
import requests

def index(request):
    form = LetterForm()
    count = None

    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.cleaned_data['letter'].lower()
            url = "https://samples.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&appid=b6907d289e10d714a6e88b30761fae22"
            response = requests.get(url, verify=False)  # Add verify=False only if needed
            data = response.json()
            cities = data.get("list", [])
            count = sum(1 for city in cities if city["name"].lower().startswith(letter))

    return render(request, 'index.html', {'form': form, 'count': count})
