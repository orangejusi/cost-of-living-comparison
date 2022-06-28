import json
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

# load data
with open('prices.json') as file:
    data = json.load(file)

# create dictionaries
hamburg = {}
berlin = {}

# save prices in seperated lists
for date in list(data.keys()):
    _hamburg = {}
    _berlin = {}
    for category in list(data[list(data.keys())[0]].keys()):
        _hamburg[category] = data[date][category][0]
        _berlin[category] = data[date][category][1]
    hamburg[date] = _hamburg
    berlin[date] = _berlin

# create table with pandas
df_ham = pd.DataFrame(hamburg).transpose()
df_ber = pd.DataFrame(berlin).transpose()

pd.options.plotting.backend = "plotly"
fig = make_subplots(rows=2, cols=1)

# create graphs via plotly
for category in list(df_ham.keys()):
    fig.add_trace(go.Scatter(x=df_ham.index, y=df_ham[category].values,
                             name='Hamburg - ' + category,
                             legendgroup=category,
                             legendgrouptitle={'text': category}), row=1, col=1)

    fig.add_trace(go.Scatter(x=df_ber.index, y=df_ber[category].values,
                             name='Berlin - ' + category,
                             legendgroup=category,
                             legendgrouptitle={'text': category}), row=2, col=1)

# show plot
fig.show()
