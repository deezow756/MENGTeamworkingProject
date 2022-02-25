
def return_interactive_graph():
  
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd  
  import mpld3
  from mpld3 import plugins
  
  # generate df
  N = 100
  df = pd.DataFrame((.1 * (np.random.random((N, 5)) - .5)).cumsum(0),
                    columns=['a', 'b', 'c', 'd', 'e'],)
  
  # plot line + confidence interval
  fig, ax = plt.subplots()
  
  fig.set_figheight(3)
  fig.set_figwidth(3)
  
  ax.grid(True, alpha=0.3)

  for key, val in df.iteritems():
      l, = ax.plot(val.index, val.values, label=key)
      ax.fill_between(val.index,
                      val.values * .5, val.values * 1.5,
                      color=l.get_color(), alpha=.4)

  # # define interactive legend

  # handles, labels = ax.get_legend_handles_labels() # return lines and labels
  # interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
  #                                                         ax.collections),
  #                                                     labels,
  #                                                     alpha_unsel=0.5,
  #                                                     alpha_over=1.5, 
  #                                                     start_visible=True)
  # plugins.connect(fig, interactive_legend)

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title('Interactive legend', size=20)

  return mpld3.fig_to_html(fig)

def return_bar_chart():
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd
  import mpld3
  from mpld3 import plugins
  
  fig = plt.figure(1, figsize=(3, 3))
  xvalues = range(5)  # the x locations for the groups

  yvalues = np.random.random_sample(5)

  width = 0.5  # the width of the bars    
  plt.title('Custom Bar Chart')
  plt.bar(xvalues, yvalues, width)

  return mpld3.fig_to_html(fig)