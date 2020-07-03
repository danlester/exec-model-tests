# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
from datetime import datetime

app = dash.Dash(__name__)

start_time = datetime.now()

app.layout = html.Div(children=[
    html.H1(children='Start time {}'.format(start_time)),

    html.Div(children='', id='outputdiv'),

    html.Button('Increment', id='button', n_clicks=0)

])

@app.callback(Output('outputdiv', 'children'), [Input('button', 'n_clicks')])
def add_sliders(n_clicks):
    return 'Clicked! Start Time {}; Count {}'.format(start_time, n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)

