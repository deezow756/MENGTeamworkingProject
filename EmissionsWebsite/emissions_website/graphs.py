from pathlib import Path
from emissions_website.settings import BASE_DIR

class Graphs():
  def return_line_chart():
    
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
    ax.set_title('Line Chart', size=20)
    ax.axis('off')

    # fig.figure.savefig(Path.joinpath(BASE_DIR, "static/media/interactivechart.png"))
    # return "media/interactivechart.png"
  
    return mpld3.fig_to_html(fig)

  def return_bar_chart():
    import matplotlib.pyplot as plt
    import numpy as np
    import mpld3
    from mpld3 import plugins
    
    barFig, ax = plt.subplots()    
    
    barFig.set_figheight(3)
    barFig.set_figwidth(3)
    
    
    # xvalues = range(5)  # the x locations for the groups
    # yvalues = np.random.random_sample(5)
    
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23,17,35,29,12]

    width = 0.5  # the width of the bars  
    ax.set_title('Bar Chart', size=20)
    ax.bar(langs,students)
    ax.axis('off')
    
    return mpld3.fig_to_html(barFig)
    
  def return_scatter_plot():
    import matplotlib.pyplot as plt
    import numpy as np
    import mpld3
    
    # Fixing random state for reproducibility
    #np.random.seed(19680801)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

    scatterFig, ax = plt.subplots()
    
    scatterFig.set_figheight(3)
    scatterFig.set_figwidth(3)
    
    ax.set_title('Scatter Plot', size=20)
    ax.scatter(x, y, s=area, c=colors, alpha=0.5)      
    ax.axis('off')
    
    return mpld3.fig_to_html(scatterFig)