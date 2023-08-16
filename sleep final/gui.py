#..............................................WEB APPLICATION........................................#

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from collections import Counter
import unicodedata
import pandas as pd
import threading
import numpy as np
import pandas as pd
import os
import base64
import joblib
import time
import pickle

app = dash.Dash()
#im1=''
#im2=''
im1=''
im2=''
im3=''
im4='https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png'
im5='https://seeklogo.com/images/S/spyder-logo-68D7CF8B2C-seeklogo.com.png'
im6=''
#im7=''
im7=''
im9=''
im8='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvba7z4hAjYvHQorXyuwqqW-HLI6olhvA2kA&usqp=CAU'



#'text': 'rgb(30, 30, 30)'
COLORS = [
    {
        'background': '#fef0d9',
        'text': 'green'
    },
    {
        'background': '#fdcc8a',
        'text': 'red'
    },
    {
        'background': '#fc8d59',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#75507B',
        'text': 'pink'
    },
    {
        'background': '#d7301f',
        'text': 'white'
    },

]
     
app.layout = html.Div([
    html.H1(children=" Bipolar Disease Detection ", style={'marginBottom': '12px','backgroundColor': COLORS[3]['background'],'color': COLORS[3]['text']}),
    html.Div(children = [html.Img(src=im1,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im2,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im3,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'})]),
    html.H2("PLEASE Answer THE DETAILS ",style={'marginBottom': '6px'}),

    html.Div(children=[dcc.Input(id = 'Year',placeholder='Year',type='number',min=0, max=2022,value=''),                
                       
                       dcc.Input(id = 'January',placeholder=' January ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'}),
                       dcc.Input(id = 'February',placeholder='  February ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'}),
                       dcc.Input(id = 'March',placeholder='  March ',type='number',min=1, max=1000,value='',style={'marginRight':'10px'})]),
                       
    
    html.Div(children=[dcc.Input(id = 'April',placeholder=' April ',type='number',min=0, max=1000,value='',style={'marginRight':'15px'}),
                       dcc.Input(id = 'May',placeholder='  May ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'}),
                       dcc.Input(id = 'June',placeholder='  June ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'}),
                       
                       dcc.Input(id = 'July',placeholder='  July ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'})]),

    html.Div(children=[dcc.Input(id = 'August',placeholder=' August ',type='number',min=0, max=1000,value='',style={'marginRight':'15px'}),
                       dcc.Input(id = 'September',placeholder='  September ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'}),
                       dcc.Input(id = 'October',placeholder='  October ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'}),
                       
                       dcc.Input(id = 'November',placeholder='  November ',type='number',min=0, max=1000,value='',style={'marginRight':'10px'})]),
    
    html.Div(children=[dcc.Input(id = 'December',placeholder=' December ',type='number',min=0, max=1000,value='',style={'marginRight':'15px'}),
                      
                       
                       ]),
    
     html.Button(id='submit-button', n_clicks=0, children='Submit', 
    style={'margintop': 15, 'marginBottom': 25}),

    
    
    html.Div(id='my-div'),
    
    html.Div(children = [html.Img(src=im6,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im7,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im9,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'})])
#], style={'textAlign': 'center'})
        
], style={'textAlign': 'center',"backgroundColor":"green"})


#"#FFE4FE"
#"#ff7700"
#"#75507B"
#"#06989A"


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks'),
     Input(component_id='Year', component_property='value'),
     Input(component_id='January', component_property='value'),
     Input(component_id='February', component_property='value'),
     Input(component_id='March', component_property='value'),
     Input(component_id='April', component_property='value'),
     Input(component_id='May', component_property='value'),
     Input(component_id='June', component_property='value'),
     Input(component_id='July', component_property='value'),
     Input(component_id='August', component_property='value'),
     Input(component_id='September', component_property='value'),
     Input(component_id='October', component_property='value'),
     Input(component_id='November', component_property='value'),
     Input(component_id='December', component_property='value'),
     
     ]
     
)
def update_output_div(n_clicks,Year,January,February,March,
                      April,May,June,
                      July,August,September,October,November,December
                      ):
    if n_clicks > 0:
        inputval=[]
        print(str(Year))
        inputval.append(str(Year))
        inputval.append(str(January))
        inputval.append(str(February))
        inputval.append(str(March))
        inputval.append(str(April))
        inputval.append(str(May))
        inputval.append(str(June))
        inputval.append(str(July))
        inputval.append(str(August))
        inputval.append(str(September))
        inputval.append(str(October))
        inputval.append(str(November))
        inputval.append(str(December))
        

        #input_data ="['Year','January','February','March','April','May','June','July','August','September','October','November','December']"
        #print('input data:',input_data)
        print(len(inputval))
        print(inputval)
        
        data=''
        for i in inputval:
            data=data+"#"+i
        data=data[1:]
        print('data',data)
        f=open('input.txt','w')
        f.write(data)
        f.close()
        f=open('check.txt','w')
        f.write('check')
        f.close()
        time.sleep(3)
        f=open('output.txt','r')
        output=f.read()
        f.close()

        clr = np.random.randint(0,4)
        return html.H2("Prediction:: "+str(output),style = {
                'backgroundColor': COLORS[0]['background'],
                'color': COLORS[clr]['text']
                })
        
if __name__ == '__main__':
    app.run_server()
        
