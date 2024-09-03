import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random


def make_web_traffic_data():
    hours = np.arange(0, 743)
    web_hits = np.random.randint(1000, 6001, 743)

    gull = web_hits[np.random.choice(hours, size=50, replace=False)]
    gull = float(np.nan)

    data = np.column_stack((hours, web_hits))

    np.savetxt('web_trafficcc.tsv', data, delimiter='\t', header='hours\tweb_hits', comments='')

    print('web_trafficci.tsv saved')



data = np.genfromtxt(r"C:\Users\user\PycharmProjects\helloworld\pythonProject\studybud\algorithms\web_trafficcc.tsv",
                     delimiter="\t")
#print(data[:10])


x = data[:, 0]
y = data[:, 1]
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]


def plot_web_traffic(x, y, models=None):
     '''
     Plot the web traffic (y) over time (x).
     If models is given, it is expected to be a list of fitted models,
     which will be plotted as well (used later in this chapter).
     '''
     plt.figure(figsize=(12,6)) # width and height of the plot in inches
     plt.scatter(x, y, s=10)
     plt.title("Web traffic over the last month")
     plt.xlabel("Time")
     plt.ylabel("Hits/hour")
     plt.xticks([w*7*24 for w in range(5)],
     ['week %i' %(w+1) for w in range(5)])
     if models:
         colors = ['g', 'k', 'b', 'm', 'r']
         linestyles = ['-', '-.', '--', ':', '-']
         mx = np.linspace(0, x[-1], 1000)
         for model, style, color in zip(models, linestyles, colors):
             plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)
             plt.legend(["d=%i" % m.order for m in models], loc="upper left")
     plt.autoscale(tight=True)
     plt.grid()

def error(f, x, y):
    return np.sum((f(x) - y) ** 2)


fp1 = np.polyfit(x, y, 1)
print("Model parameters: %s" % fp1)

f1 = np.poly1d(fp1)
print(error(f1, x, y))

f2p = np.polyfit(x,y,2)
print(f2p)


f2=np.poly1d(f2p)
print(error(f2, x, y))

f3p =np.polyfit(x,y,3)
print(f3p)

f3=np.poly1d(f3p)
print(error(f3,x,y))

f10p =np.polyfit(x,y,10)
print(f10p)

f10=np.poly1d(f10p)
print(error(f10,x,y))

f53p=np.polyfit(x,y,53)
print(f53p)

f53=np.poly1d(f53p)
print(error(f53,x,y))

f100p=np.polyfit(x,y,100)
print(f100p)

f100=np.poly1d(f100p)
print(error(f100,x,y))


plot_web_traffic(x, y, [f1,f2,f3,f10,f53,f100])

print("Error for the complete data set:")
for f in [f1,f2,f3,f10,f53,f100]:
    print("td=%i: %f" % (f.order, error(f,x,y)))

