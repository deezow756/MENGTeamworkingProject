from pathlib import Path
from emissions_website.settings import BASE_DIR

class Map():
    def generate_map():
        import geopandas as pnd
        import geoplot
        import pandas as pd
        import mapclassify as mc
        import mpld3
        import plotly.express as px
        import plotly.io as io

        # Get data to test function.
        world = pnd.read_file(
            pnd.datasets.get_path('naturalearth_lowres')
        )

        world.sort_values(by=['name'])
        world['name'] = world['name'].str.upper()

        data2014 = pd.read_csv(Path.joinpath(BASE_DIR, "static/data/2014.csv"))
        totalEmissions = data2014[['Country','Total']]

        #emissionWorld = pd.merge(world, totalEmissions, how='inner', left_on='name', right_on='Country')

        # This defines the bins into which countries are sorted by emission totals.
        bins = [1000, 10000, 50000, 100000, 500000, 1000000, 10000000]
        # This sets these bins as the custom scheme.
        #scheme = mc.UserDefined(emissionWorld['Total'], bins)
        
        
        fig = px.choropleth(totalEmissions, width=1200, height=700 , color="Total", color_continuous_scale="rdylgn_r"
                            , labels={"Total" : "Emissions Scale"}, locations="Country", locationmode="country names"
                            , hover_data={"Country", "Total"}, range_color=[1, 3000000], )
        fig.update_layout(paper_bgcolor="#E8E8E8")
        return io.to_html(fig)

        # Draw map with geoplot.
        # mapFig = geoplot.choropleth(
        #     emissionWorld, hue='Total', figsize=(12, 7), scheme=scheme, legend=True
        # )      
               
        #return mpld3.fig_to_html(mapFig.figure)
        
    def generate_map_year(year):
        
        import geopandas as pnd
        import pandas as pd
        import plotly.express as px
        import plotly.io as io

        # Get data to test function.
        world = pnd.read_file(
            pnd.datasets.get_path('naturalearth_lowres')
        )

        world.sort_values(by=['name'])
        world['name'] = world['name'].str.upper()

        data2014 = pd.read_csv(Path.joinpath(BASE_DIR, "static/data/" + year +".csv"))
        totalEmissions = data2014[['Country','Total']]
        
        highest = totalEmissions.nlargest(n=1, columns=['Total'])
        
        maxRange = int(highest['Total'])
        
        fig = px.choropleth(totalEmissions, height=600 , color="Total", color_continuous_scale="rdylgn_r"
                            , labels={"Total" : "Emissions"}, locations="Country", locationmode="country names"
                            , hover_data={"Country", "Total"}, range_color=[1, maxRange], )
        fig.update_layout(paper_bgcolor="#E8E8E8")
        return io.to_html(fig)