import plotly.figure_factory as ff
import statistics 
import random 
import pandas as pd 
import csv 
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of population",mean)
print("stadard deviation of population",std_deviation)
#fig = ff.create_distplot([data],["temp"],show_hist = False)
#fig.show()
dataset = []
for i in range (0,100):
    randomIndex = random.randint(0,len(data)-1)
    value = data[randomIndex]
    dataset.append(value)

mean1 = statistics.mean(dataset)
std_deviation1 = statistics.stdev(dataset)
print("mean of sample",mean1)
print("stadard deviation of sample",std_deviation1)

def randomset_of_mean(counter):
    dataset = []
    for i in range (0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([data],["temp"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.2],mode = "lines",name = "mean"))
    fig.show()     
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = randomset_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean",mean)
setup()
