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
    
    fig = px.bar(x=top10["Country"], y=top10["Total"], title="Top 10 Countries With The Highest Emissions")
    fig.update_layout(paper_bgcolor="#E8E8E8")
    fig.update_layout(title_text='Top 10 Countries With The Highest Emissions', title_x=0.5)
    fig.update_xaxes(title= "", visible=True, showticklabels=True)
    fig.update_yaxes(title= "", visible=True, showticklabels=True)
    
    return io.to_html(fig)
    
  def generate_pie_chart(year):
    import pandas as pd
    import plotly.express as px
    import plotly.io as io    
    
    data2014 = pd.read_csv(Path.joinpath(BASE_DIR, "static/data/" + year + ".csv"))
    totalEmissions = data2014[['Country','Total']]
    
    top20 = totalEmissions.nlargest(n=20, columns=['Total'])
    
    fig = px.pie(top20, values="Total", names="Country")
    fig.update_layout(paper_bgcolor="#E8E8E8")
    fig.update_layout(title_text='Top 20 Countries With The Highest Emissions', title_x=0.5)
    
    return io.to_html(fig)
