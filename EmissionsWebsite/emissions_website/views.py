from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .graphs import Graphs
from .map import Map
from django.http import JsonResponse

maps = {}
barCharts = {}
pieCharts = {}

def index(request):
  
  index = 1990
  for x in range(41):
    maps[str(index)] = Map.generate_map_year(str(index))
    barCharts[str(index)] = Graphs.generate_bar_chart(str(index))
    pieCharts[str(index)] = Graphs.generate_pie_chart(str(index))
    index += 1
    
  mapchart = maps["2002"]
  barchart = barCharts["2002"]
  pieChart = pieCharts["2002"]
    
  return render(request, "index.html", context={'mapchart': mapchart, 'barchart': barchart, 'piechart': pieChart}) 

def update(request):
  year = request.GET.get('year', None)
  data = {
        'map': maps[year],
        'bar': barCharts[year],
        'pie': pieCharts[year]
  }
  return JsonResponse(data)