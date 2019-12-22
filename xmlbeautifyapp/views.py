from django.shortcuts import render
from .xmlbeautifylogic import xml_beautify

def index(request):
    return render(request, 'xmlbeautifyapp/index.html')

def about(request):
    return render(request, 'xmlbeautifyapp/about.html')

def output(request):
    given_xml_str = str(request.GET['xml_code'])
    formatted_xml_str = xml_beautify(given_xml_str)
    return render(request, 'xmlbeautifyapp/output.html', {'formatted_xml_str':formatted_xml_str})
