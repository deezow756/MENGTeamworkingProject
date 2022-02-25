from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import graphs


def index(request):
  barchart = graphs.return_bar_chart()
  linechart = graphs.return_interactive_graph()
  newchart = graphs.return_bar_chart()
    
  return render(request, "index.html", {'barchart': barchart, 'linechart': linechart, 'newchart': newchart}) 
  