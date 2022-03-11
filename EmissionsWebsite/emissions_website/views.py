from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .graphs import Graphs
from .map import Map


def index(request):
  
  mapchart = Map.generate_map()
  barchart = Graphs.return_bar_chart()
  linechart = Graphs.return_line_chart()
  scatterchart = Graphs.return_scatter_plot()
    
  return render(request, "index.html", context={'mapchart': mapchart, 'barchart': barchart, 'linechart': linechart, 'scatterchart': scatterchart}) 
  