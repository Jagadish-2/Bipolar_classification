#......................................Web Application.................................................#

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from collections import Counter
import unicodedata
#import plotly.plotly as py
import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd
from random import randint
import threading
import pandas as pd
import os
import numpy as np
import base64
import joblib
from tkinter import filedialog
from tkinter import *

app = dash.Dash()
im1='https://www.researchgate.net/profile/Veronica-Medina/publication/289984682/figure/fig2/AS:320007922831363@1453307242393/The-electrode-configuration-used-in-the-current-study-The-EEG-was-acquired-by-10.png'
im2='https://www.shutterstock.com/image-illustration/medically-3d-illustration-shows-sleeping-snoring-1808564095.png'
#im2='https://media.sciencephoto.com/image/m4000137/800wm'
im3='https://www.shutterstock.com/image-vector/sleep-apnea-vector-icon-illustration-600w-723438508.jpg'
im4='https://upload.wikimedia.org/wikipedia/en/c/cd/Anaconda_Logo.png'
im5='https://seeklogo.com/images/S/spyder-logo-68D7CF8B2C-seeklogo.com.png'
im6='https://www.englewooddental.com/files/2019/03/Blog-Graphics-768x768.png'
im7='https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Plotly-logo-01-square.png/220px-Plotly-logo-01-square.png'
im8='https://cdn0.iconfinder.com/data/icons/trending-tech/94/artificial_intelligence-512.png'
im9 ='https://cdn-images-1.medium.com/max/1200/1*lkqc68a6b7_TLALs5fmI6A.png'
clf=joblib.load('Best_Model_final.pkl')
        

app.layout = html.Div([
    html.H1(children=' EEG Sleep  Apnea Detection using MACHINE LEARNING', style={'marginBottom': '12px'}),
    html.Div(children = [html.Img(src=im1,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im2,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im3,style={'width': '20%', 'marginLeft': 'auto', 'marginRight': 'auto'})]),
    html.H2(" SELECT EEG SLEEP SIGNAL TO TEST ",style={'marginBottom': '6px'}),    
    html.Button(id='submit-button', n_clicks=0, children='UPLOAD THE EEG BRAINWAVE SENSOR DETAILS', 
    style={'marginTop': 15, 'marginBottom': 25}),
    html.Div(id='my-div'),
    html.Div(children = [html.Img(src=im6,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im7,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                         html.Img(src=im9,style={'width': '25%', 'marginLeft': 'auto', 'marginRight': 'auto'})])
], style={'textAlign': 'center',"backgroundColor":"#06989A"})
#], style={'textAlign': 'center',"backgroundColor":"#06989A"})
#"#FFE4FE"
#"#ff7700"
#"#75507B"
#"#06989A"

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')]
)
def update_output_div(n_clicks):
    if n_clicks > 0:
        root = Tk()
        path = 'H:/2023 Projects/Sleep_Apnea/sleep final/EEG_BrainwaveSensor_Test'
        root.filename =  filedialog.askopenfilename(initialdir = path,title = "Select file",filetypes = (("EEG files","*.csv"),("all files","*.*")))
        print (root.filename)
        root.destroy()

        df = pd.read_csv(root.filename)
        X= df.values
        print(X)
        Class = clf.predict(X)
        print('Class:',Class)

        new_prob = clf.predict_proba(X)
        test_confidance = 100*np.max(new_prob)
        acc = "{:.0f}".format(test_confidance)
        #print('acc:',acc)
        accuracy = "{:2f}%".format(test_confidance)
        print("Test_Accuracy:",accuracy)
        cs = 'Test confidance',accuracy
    
        if int(Class[0]) == 0:
            print('#Sleep apnia stage 1')
            if int(acc) >=50:
                return html.H1(children='Selected EEG_Sleep level is:Deeper sleep  ' + str(cs), style={'marginBottom': '10px'})
            else:
                return html.H1(children='Selected EEG_Sleep level is:REM sleep  ' + str(cs), style={'marginBottom': '10px'})
        
        elif int(Class[1]) == 1:
            print('#Sleep apnea stage 2')
            if int(acc) >=50:
                return html.H1(children='Selected EEG_Sleep level is:Obstructive sleep  ' + str(cs), style={'marginBottom': '10px'})
            else:
                return html.H1(children='Selected EEG_Sleep level is:slow wave sleep  ' + str(cs), style={'marginBottom': '10px'})
                
        elif int(Class[2]) == 2:
            print('#Sleep apnea stage 2')
            if int(acc) >=50:
                return html.H1(children='Selected EEG_Sleep level is:center sleep apnea  ' + str(cs), style={'marginBottom': '10px'})
            else:
                return html.H1(children='Selected EEG_Sleep level is:Complex sleep apnea syndrome  ' + str(cs), style={'marginBottom': '10px'})
        elif int(Class[3]) == 3:
            print('#Sleep apnea stage 2')
            if int(acc) >=50:
                return html.H1(children='Selected EEG_Sleep level is:Catathrenia  ' + str(cs), style={'marginBottom': '10px'})
            else:
                return html.H1(children='Selected EEG_Sleep level is:sleep ' + str(cs), style={'marginBottom': '10px'})
        else:
            return html.H1(children='Selected EEG_Sleep level is: Not recognised  ' + str(cs), style={'marginBottom': '10px'})
        
if __name__ == '__main__':
    app.run_server()
        
