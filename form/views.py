from re import template
from django.shortcuts import render
from django.views import *
from django.http import JsonResponse
from django.shortcuts import render
import urllib.request
import json
# Create your views here.

class FormView(View):
    template_name = 'index.html'

    def get(self, request):
        url = 'http://127.0.0.1:8000/static/jsondata/countries.json/'
        with urllib.request.urlopen(f"{url}") as u:
            data = json.loads(u.read().decode())
        return render(request, 'index.html', {'country': data})
        # return render(request, self.template_name, {})


# class CountryData(View):
#     def get(self, request):

#         url = 'http://127.0.0.1:8000/static/jsondata/countries.json/'
#         with urllib.request.urlopen(f"{url}") as u:
#             data = json.loads(u.read().decode())
#         return render(request, 'index.html', {'country': data})



class SatetData(View):

    def get(self, request):
        country_id = request.GET.get('CountryId',"")
       
        state_data = open('form\static\jsondata\states.json', "r", encoding="utf8")
        json_statesdata = json.load(state_data)
        
        selectedCountryData = [stateData for stateData in json_statesdata if stateData['country_id'] == int(country_id)]
        return JsonResponse(data=selectedCountryData, safe=False)
