from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import graphs


def index(request):
  graph = graphs.return_interactive_graph()
    
  return render(request, "index.html", {'chart': graph}) 
  