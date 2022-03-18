from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .graphs import Graphs
from .map import Map
from django.http import JsonResponse

maps = {}
barCharts = {}

def index(request):
  
  index = 1990
  for x in range(25):
    maps[str(index)] = Map.generate_map_year(str(index))
    barCharts[str(index)] = Graphs.generate_bar_chart(str(index))
    index += 1
    
  mapchart = maps["2002"]
  barchart = barCharts["2002"]
  #linechart = Graphs.return_line_chart()
  #scatterchart = Graphs.return_scatter_plot()
    
  return render(request, "index.html", context={'mapchart': mapchart, 'barchart': barchart}) 

def update(request):
  year = request.GET.get('year', None)
  data = {
        'map': maps[year],
        'bar': barCharts[year]
  }
  return JsonResponse(data)