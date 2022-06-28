import plotly.express as px

# create list for axis ordered by cities
hamburg_x, hamburg_y, berlin_x, berlin_y = [], [], [], []

# open file and read x and y value for Hamburg and Berlin
with open('Hamburg.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        _x, _y = i.split('/')
        hamburg_y.append(float(_y))
        hamburg_x.append(_x)

with open('Berlin.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        _x, _y = i.split('/')
        berlin_y.append(float(_y))
        berlin_x.append(_x)


# plot graph using plotly
fig = px.line(x=hamburg_x, y=hamburg_y, markers=True)
fig.add_scatter(x=berlin_x, y=berlin_y)
fig.show()
