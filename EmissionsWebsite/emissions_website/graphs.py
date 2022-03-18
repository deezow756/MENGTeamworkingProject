from pathlib import Path
from tkinter import Y

from mpld3 import fig_to_html

from emissions_website.settings import BASE_DIR


class Graphs():
  
  def return_bar_chart():
    import pandas as pd
    import plotly.express as px
    import plotly.io as io
    
    data2014 = pd.read_csv(Path.joinpath(BASE_DIR, "static/data/2014.csv"))
    totalEmissions = data2014[['Country','Total']]
    
    top10 = totalEmissions.nlargest(n=10, columns=['Total'])
    
    top10 = top10.iloc[::-1]   
    
    print(top10)
    
    fig = px.bar(x=top10["Country"], y=top10["Total"])
    fig.update_layout(paper_bgcolor="#E8E8E8")
    fig.update_xaxes(title= "", visible=True, showticklabels=True)
    fig.update_yaxes(title= "", visible=True, showticklabels=True)
    
    return io.to_html(fig)
  
  def generate_bar_chart(year):
    import pandas as pd
    import plotly.express as px
    import plotly.io as io
    
    data2014 = pd.read_csv(Path.joinpath(BASE_DIR, "static/data/" + year + ".csv"))
    totalEmissions = data2014[['Country','Total']]
    
    top10 = totalEmissions.nlargest(n=10, columns=['Total'])
    
    top10 = top10.iloc[::-1]   
    
    fig = px.bar(x=top10["Country"], y=top10["Total"])
    fig.update_layout(paper_bgcolor="#E8E8E8")
    fig.update_xaxes(title= "", visible=True, showticklabels=True)
    fig.update_yaxes(title= "", visible=True, showticklabels=True)
    
    return io.to_html(fig)
    
  def return_scatter_plot():
    import matplotlib.pyplot as plt
    import numpy as np
    
    return
    
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
