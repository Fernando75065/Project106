import csv 
import pandas as ps
import plotly_express as px
import numpy as np

def plotFigure(path):
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile)
        scatter = px.scatter(reader, x='Temperature', y='Ice-cream Sales( ₹ )')
        scatter.show()

def dataA(path):
    iceCreamSales=[]
    Temperature=[]
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            Temperature.append(float(row['Temperature']))
            iceCreamSales.append(float(row['Ice-cream Sales( ₹ )']))
    return{'x' : Temperature, 'y':iceCreamSales}

def findCorrelation(data):
    correlation = np.corrcoef(data['x'], data['y'])
    print('correlation between temperature vs icecream sales = \n', correlation[0,1])

def setup():
    path='data.csv'
    f =dataA(path)
    findCorrelation(f)
    plotFigure(path)
setup()