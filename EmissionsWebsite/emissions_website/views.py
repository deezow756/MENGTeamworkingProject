from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .graphs import Graphs
from .map import Map
from django.http import JsonResponse


def index(request):
  
  mapchart = Map.generate_map()
  barchart = Graphs.return_bar_chart()
  #linechart = Graphs.return_line_chart()
  scatterchart = Graphs.return_scatter_plot()
    
  return render(request, "index.html", context={'mapchart': mapchart, 'barchart': barchart, 'scatterchart': scatterchart}) 

def update(request):
  year = request.GET.get('year', None)
  data = {
        'map': Map.generate_map_year(year),
        'bar': Graphs.generate_bar_chart(year)
  }
  return JsonResponse(data)