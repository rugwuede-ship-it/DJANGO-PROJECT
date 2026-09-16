from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def record(request):
  template = loader.get_template('record/record.html')
  return HttpResponse(template.render())
def name(request):
    return HttpResponse("Hello, Rhema!")
def greet(request, name):
    return render(request, 'record/greet.html', {'name': name.capitalize()})
#You can choose to either use the render function or the loader function to render the template. The render function is a shortcut that combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text. The loader function is used to load a template from the filesystem and return a Template object, which can then be rendered with a context dictionary.