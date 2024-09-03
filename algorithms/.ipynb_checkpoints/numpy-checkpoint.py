import numpy as np
import scipy
import matplotlib.pyplot as plt

sum = np.genfromtxt("web_traffic.tsv", delimiter="\t")
data=sum.reshape(30,2)
x=data[:,0]
y=data[:,1]
x=x[~np.isnan(y)]
y=y[~np.isnan(y)]


def plot_web_traffic(x,y, models):
    """
    plot the web traffic (y) over time (x)
    if models is given, it is expected to be a list of fitted models,
    which will be plotted as well (used later in this chapter).
    """
    plt.figure(figsize=(12,6))#width and height of the plot in inches
    plt.scatter(x,y,s=10)
    plt.title("Web Traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w*7*24 for w in range(5)],
               ['week %i' %(w+1) for w in range(5)])
    if models:
        colors =['g','k','b','m','r']
        linestyles = ['-','-.','--',':','-']

        mx =sp.linspace(0,x[-1],1000)
        for model,style,color in zip(models,linestyles,colors):
            plt.plot(mx,model(mx),linestyle=style,color=color)
            