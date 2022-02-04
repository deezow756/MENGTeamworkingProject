from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
from io import StringIO

# Define some CSS to control our custom labels
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

def index(request):
    #fig, ax = plt.subplots()
    #ax.grid(True, alpha=0.3)

    #N = 50
    #df = pd.DataFrame(index=range(N))
    #df['x'] = np.random.randn(N)
    #df['y'] = np.random.randn(N)
    #df['z'] = np.random.randn(N)

    #labels = []
    #for i in range(N):
        #label = df.iloc[[i], :].T
        #label.columns = ['Row {0}'.format(i)]
        # .to_html() is unicode; so make leading 'u' go away with str()
        #labels.append(str(label.to_html()))

    #points = ax.plot(df.x, df.y, 'o', color='b',
                 #mec='k', ms=15, mew=1, alpha=.6)

    #ax.set_xlabel('x')
    #ax.set_ylabel('y')
    #ax.set_title('HTML tooltips', size=20)

    #graph_div = plotly.offline.plot(fig, auto_open = False, output_type="div")
    graph = return_graph()
    
    return render(request, "index.html", {'chart': graph})
  
def return_graph():

  x = np.arange(0,np.pi*3,.1)
  y = np.sin(x)

  fig = plt.figure()
  plt.plot(x,y)

  imgdata = StringIO()
  fig.savefig(imgdata, format='svg')
  imgdata.seek(0)

  data = imgdata.getvalue()
  return data