import csv 
import pandas as ps
import plotly_express as px
import numpy as np
import plotly.figure_factory as pff

def plotFigure(path):
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile)
        scatter = px.scatter(reader, x='Coffee in ml', y='sleep in hours')
        scatter.show()

def dataA(path):
    Coffee=[]
    Sleep=[]
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            Coffee.append(float(row['Coffee in ml']))
            Sleep.append(float(row['sleep in hours']))
    return{'x' : Coffee, 'y':Sleep}

def findCorrelation(data):
    correlation = np.corrcoef(data['x'], data['y'])
    print('correlation between coffee consumption vs sleep = \n', correlation[0,1])

def setup():
    path='coffee.csv'
    f =dataA(path)
    findCorrelation(f)
    #plotFigure(path)
setup()

reader=ps.read_csv('coffee.csv')
normalDistribution=pff.create_distplot([reader['Coffee in ml'].tolist()],['Coffee'],show_hist=False)
normalDistribution.show()