To run the web server:
1. make sure you install the following libraies:

conda update
conda install -c anaconda django
conda install -c conda-forge matplotlib
conda install -c anaconda pandas
conda install --channel conda-forge geopandas
conda install -c plotly plotly

2. in the terminal type: cd EmissionsWebsite
    then type: python manage.py runserver

3. open your browser and in the url type: localhost:8000

4. after making a change just save the file you changed and refresh the browser

5. to stop the server from running: in the terminal press Ctrl + C