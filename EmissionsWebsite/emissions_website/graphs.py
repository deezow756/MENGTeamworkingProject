import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import pandas as pd
from io import StringIO
import mpld3
from mpld3 import plugins
np.random.seed(9615)

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

def return_interactive_graph():
  # generate df
  N = 100
  df = pd.DataFrame((.1 * (np.random.random((N, 5)) - .5)).cumsum(0),
                    columns=['a', 'b', 'c', 'd', 'e'],)
  
  # plot line + confidence interval
  fig, ax = plt.subplots()
  ax.grid(True, alpha=0.3)

  for key, val in df.iteritems():
      l, = ax.plot(val.index, val.values, label=key)
      ax.fill_between(val.index,
                      val.values * .5, val.values * 1.5,
                      color=l.get_color(), alpha=.4)

  ## define interactive legend

  #handles, labels = ax.get_legend_handles_labels() # return lines and labels
  #interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
                                                          #ax.collections),
                                                      #labels,
                                                      #alpha_unsel=0.5,
                                                      #alpha_over=1.5, 
                                                      #start_visible=True)
  #plugins.connect(fig, interactive_legend)

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title('Interactive legend', size=20)

  return mpld3.fig_to_html(fig)