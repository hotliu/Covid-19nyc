# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go
import pandas as pd



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             #### Your Value Proposition

#             Emphasize how the app will benefit users. Don't emphasize the underlying technology.

#             ✅ RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

#             ❌ RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

#             """
#         ),
#         dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
#     ],
#     md=2,
# )


table_data = [['Team', 'Wins', 'Losses'],
              ['Montréal<br>Canadiens', 18, 4],
              ['Dallas Stars', 18, 5],
              ['NY Rangers', 16, 5],
              ['Boston<br>Bruins', 13, 8],
              ['Chicago<br>Blackhawks', 13, 8],
              ['LA Kings', 13, 8],
              ['Ottawa<br>Senators', 12, 5],
              ['Boston<br>Bruins', 13, 8],
              ['Chicago<br>Blackhawks', 13, 8],
              ['LA Kings', 13, 8],
              ['Ottawa<br>Senators', 12, 5]]

fig4 = ff.create_table(table_data, height_constant=60)

# Update the margins to add a title and see graph x-labels.
fig4.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 50})

# import plotly.graph_objects as go
# from plotly.colors import n_colors
# import numpy as np
# np.random.seed(1)

# colors = n_colors('rgba(255, 255, 255, 0)', 'rgba(205, 248, 215, 0.6)', 9, colortype='rgb')
# a = np.random.randint(low=0, high=9, size=10)
# b = np.random.randint(low=0, high=9, size=10)
# c = np.random.randint(low=0, high=9, size=10)

# fig4 = go.Figure(data=[go.Table(
#   header=dict(
#     values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
#     line_color='white', fill_color='white',
#     align='center',font=dict(color='rgba(50, 112, 90, 0.8)', size=23)
#   ),
#   cells=dict(
#     values=[a, b, c],
#     line_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
#     fill_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
#     align=['center', 'center'], font=dict(color='rgba(50, 112, 90, 0.8)', size=30), height = 80
#     ))
# ])
# fig4.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 60})



# gapminder = px.data.gapminder()
# fig1 = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)



mapbox_access_token = "pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txcjE4NDAwNngzZms0ZndzNGM3dG0ifQ.gXrN0wMYVhqUp7t1LOHEwA"
#open(".mapbox_token").read()

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-16-2020.csv')

fig1 = go.Figure()

fig1 = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_data=["Country/Region",'Confirmed', 'Deaths'],
                        size='Confirmed', zoom=2, color = 'Confirmed', color_continuous_scale=px.colors.sequential.Purp, size_max=50,height=800)

fig1.update_layout(
    mapbox_style="white-bg",
    hovermode='closest',
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://api.mapbox.com/styles/v1/lilysu/ck7v7bqqy08ae1irye0k0jcot/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
            ] 
        },
        # {
        #     "sourcetype": "raster",
        #     "source": ["https://geo.weather.gc.ca/geomet/?"
        #                "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
        #                "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
        # }
      ])
fig1.update_layout(margin={"r":80,"t":0,"l":0,"b":30})





x1 = np.random.randn(200)
x2 = np.random.randn(200) + 2

group_labels = ['Group 1', 'Group 2']

colors = ['#7FA6EE', '#B8F7D4']

# Create distplot with curve_type set to 'normal'
fig2 = ff.create_distplot([x1, x2], group_labels, bin_size=.5,
                         curve_type='normal', # override default 'kde'
                         colors=colors)

# Add title
fig2.update_layout(title_text='Distplot with Normal Distribution')
# fig.show()





fig3 = go.Figure()
fig3.add_trace(go.Bar(
    name='Control',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[3, 6, 4],
    error_y=dict(type='data', array=[1, 0.5, 1.5])
))
fig3.add_trace(go.Bar(
    name='Experimental',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[4, 7, 3],
    error_y=dict(type='data', array=[0.5, 1, 2])
))
fig3.update_layout(barmode='group')
# fig.show()


column1 = dbc.Col(
    [
        dcc.Graph(figure=fig4),
    ],
    md=3,
)


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig1),
    ],
    md=9,
)

column3 = dbc.Col(
    [
        dcc.Graph(figure=fig2),
    ]
)

column4 = dbc.Col(
    [
        dcc.Graph(figure=fig3),
    ]
)

# layout = dbc.Row([column1, column2])
layout = [dbc.Row([column1, column2]), 
        dbc.Row([column3]),
        dbc.Row([column4]),]

