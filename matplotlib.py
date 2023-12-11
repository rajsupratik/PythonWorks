import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Drawing a line Diagram
xpoint = np.array([0,6])
ypoint = np.array([50,250])

plt.plot(xpoint,ypoint,'-.')    
plt.show()

xpoint = np.array([1,2,6,8])
ypoint = np.array([3,8,1,10])

plt.plot(xpoint,ypoint,'-.')    
plt.show()

## plot() - to plot the graph
## show() - to display the graph
## title() - to give a title to the graph
## xlabel() - gives label to the xaxis
## ylabel() - gives label to the y sxis
## savefig() - to save the result in a file
## legend() - to apply legend in a chart
## subplot() - in this you can specify rows, column and then the third argument will be index
## scatter() - draws a scatter plot
## bar() - to draw bar graphs
## barh() - for horizontal bar graphs
## hist() - for histograms
## pie() - for pie charts

# scatter Chart
x = np.array([5,8,7,5,1,4,9,12,6])
y = np.array([99,78,67,98,91,88,76,84,122])
plt.scatter(x,y,color='red')
x = np.array([51,18,17,15,1,2,3,19,7])
y = np.array([100,108,97,68,111,78,96,104,142])
plt.scatter(x,y,color='green')
plt.xlabel("age")
plt.ylabel("speed") 
plt.legend('day1','day2')
plt.show()

# Bar Graph

a = np.array(["A","B","C","D"])
b = np.array([3,8,1,10])
plt.bar(x,y,color = 'blue')
plt.show()

# pie Charts

i = np.array([35,25,15,25])
mylabels = ["apples","bananas","Grapes","Mangoes"]

myexplode = [0.2,0,0,0]
mycolor = ["black","hotpink","b","#4CAF50"]

plt.pie(i,labels=mylabels,explode=myexplode,shadow=True,colors=mycolor)
plt.legend(title = "Four Fruits")
plt.show()
