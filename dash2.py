from ctypes import alignment
from turtle import width
import pandas as pd
import plotly.express as px
from subprocess import call
import dash
import dash_core_components as dcc
from dash import dash_table
from dash.dash_table.Format import Group
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os
import dash_auth
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
server = app.server

auth = dash_auth.BasicAuth(
    app,
    {'sahil': '0000'}
)

df = pd.read_csv("./links.csv")

dff = df.groupby('SN', as_index=False)[['TITLE','URL']].sum()
scriptpy = "automation-tut4.py"
# ---------------------------------------------------------------
app.layout = html.Div([ 
    html.Br(),
    html.Div([
        
        dash_table.DataTable(
            id='table', 
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": True} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            css=[{'selector': 'tr:hover','rule': 'background-color:  #80FF80',}],
            page_action="native",
            page_current=0,
            page_size=6,
            # page_action='none',
            # style_cell={
            # 'whiteSpace': 'normal'
            # },
            # fixed_rows={ 'headers': True, 'data': 0 },
            # virtualization=False,
            style_cell_conditional=[
                {'if': {'column_id': 'SN'},
                 'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'TITLE'},
                 'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'URL'},
                 'width': '60%', 'textAlign': 'left'},
            ],
        ),
        html.Div(id='hidden-div', style={'display': 'none'})
    ],className='row'),

    dbc.Button("Submit",id='pass_index', color="green", className="btn-success", size="lg"),
  
])

@app.callback(
    Output('hidden-div','style'),
    Input('pass_index', component_property='n_clicks')
)

def print_value(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return os.system(f"python {scriptpy}")
        
if __name__ == '__main__':
    app.run_server(debug=True)