import matplotlib.pyplot as plt

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

# plot graph using matplotlib
plt.xlabel('Date')
plt.ylabel('Price')
plt.plot(hamburg_x, hamburg_y, hamburg_x, hamburg_y, 'oy', hamburg_x, hamburg_y, hamburg_x, hamburg_y, 'or')
plt.plot(berlin_x, berlin_y, berlin_x, berlin_y, 'o', berlin_x, berlin_y, berlin_x, berlin_y, color='b')
plt.show()
