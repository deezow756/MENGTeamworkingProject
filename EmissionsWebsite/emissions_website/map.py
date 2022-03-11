from pathlib import Path
from emissions_website.settings import BASE_DIR

class Map():
    def generate_map():
        import geopandas as pnd
        import geoplot
        import pandas as pd
        import mapclassify as mc
        import mpld3

        # Get data to test function.
        world = pnd.read_file(
            pnd.datasets.get_path('naturalearth_lowres')
        )

        world.sort_values(by=['name'])
        world['name'] = world['name'].str.upper()

        data2014 = pd.read_csv(Path.joinpath(BASE_DIR, "static/data/2014.csv"))
        totalEmissions = data2014[['Country','Total']]

        emissionWorld = pd.merge(world, totalEmissions, how='inner', left_on='name', right_on='Country')

        # This defines the bins into which countries are sorted by emission totals.
        bins = [1000, 10000, 50000, 100000, 500000, 1000000, 10000000]
        # This sets these bins as the custom scheme.
        scheme = mc.UserDefined(emissionWorld['Total'], bins)

        # Draw map with geoplot.
        mapFig = geoplot.choropleth(
            emissionWorld, hue='Total', figsize=(12, 7), scheme=scheme, legend=True
        )    
        
        

        # mapFig.figure.savefig(Path.joinpath(BASE_DIR, "static/media/2014Map.png"))
        # return "media/2014Map.png"       
        
        
        return mpld3.fig_to_html(mapFig.figure)
        