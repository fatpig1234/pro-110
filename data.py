import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv


df= pd.read_csv("medium_data.csv")
data= df["average"].tolist()


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean



def setup():
    meanlist=[]
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        meanlist.append(set_of_means)


def show_fig(meanlist):
    df = meanlist
    fig = ff.create_distplot(([df]), ['temp'] , show_hist=False )
    fig.show