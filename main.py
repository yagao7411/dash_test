# dev now
#obj: a test dash to run in gcp
#ref: https://datasciencecampus.github.io/deploy-dash-with-gcp/

#check Python verion
import sys
import dash
print('here here')
print(sys.version)
print(dash.__version__)


#get lib
import os
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# Expose Flask instance
server = app.server

#read data
csv_files_path = os.path.join('data/1.csv')
df = pd.read_csv(csv_files_path)

#setup the figure
fig = px.bar(
    df, 
    x="Fruit", y="Amount", color="City", barmode="group"
)

#layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash Ya Gao'),

    html.Div(children='''
        Dash: A web application framework for Python. Customized right here!
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# -------------------------- MAIN ---------------------------- #
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)