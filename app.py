# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Test Data Viz'),
    
    html.Div(children='''
        This is a Dash mockup of the data visualizations. It pulls data I made up from a .csv to represent what you might want. There are a few ways to use Dash. I personally prefer using JupyterLab to create this because JupyterLab allows me to have a terminal open next to my app, so I can edit the .py and run in the terminal separately. This could be done in an .ipynb, but it would not have the benefit of running an active terminal, which reloads the webapp when it detects changes to the .py
    '''),
    
    dcc.Slider(
        id='test-slider-1',
        min=0.1,
        max=1,
        step=0.1,
        value=0.5
        
    ),
    
    dcc.Slider(
        id='test-slider-2',
        min=0,
        max=1,
        step=0.1,
        value=0.2
    ),
    
    dcc.Slider(
        id='test-slider-3',
        min=0,
        max=10,
        step=1,
        value=5
    ),
    
    dcc.Graph(
        id='example-graph-1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'this'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
